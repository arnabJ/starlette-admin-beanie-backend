from typing import Any, Sequence, Type
from uuid import UUID

import bson
import pydantic
from beanie import Document, PydanticObjectId
from pydantic import Field
from starlette_admin import BaseField, StringField, IntegerField, DecimalField, EmailField, URLField
from starlette_admin.converters import StandardModelConverter, converts
from starlette_admin.exceptions import (
    NotSupportedAnnotation as BaseNotSupportedAnnotation,
)

from .exceptions import NotSupportedAnnotation


class BaseODMModelConverter(StandardModelConverter):
    def get_type(self, model: Document, value: Any) -> Any:
        if isinstance(value, str) and hasattr(model, value):
            return model.model_fields[value].annotation
        raise ValueError(f"Can't find attribute with key {value}")

    def convert_fields_list(
        self, *, fields: Sequence[Any], model: Type[Document], **kwargs: Any
    ) -> Sequence[BaseField]:
        fields = [v for v in fields]
        try:
            return super().convert_fields_list(fields=fields, model=model, **kwargs)
        except BaseNotSupportedAnnotation as e:
            raise NotSupportedAnnotation(*e.args) from e


class ModelConverter(BaseODMModelConverter):
    @converts(Field)
    def conv_odm_field(self, *args: Any, type: Field, **kwargs: Any) -> BaseField:
        kwargs.update(
            {
                "type": type.pydantic_field.annotation,
                "required": type.is_required_in_doc() and not type.primary_field,
            }
        )
        return self.convert(*args, **kwargs)

    @converts(bson.ObjectId, bson.Regex, bson.Binary, pydantic.NameEmail, PydanticObjectId, UUID)
    def conv_bson_string(self, *args: Any, **kwargs: Any) -> BaseField:
        return StringField(**self._standard_type_common(**kwargs))

    @converts(bson.Int64)
    def conv_bson_int64(self, *args: Any, **kwargs: Any) -> BaseField:
        return IntegerField(**self._standard_type_common(**kwargs))

    @converts(bson.Decimal128)
    def conv_bson_decimal(self, *args: Any, **kwargs: Any) -> BaseField:
        return DecimalField(**self._standard_type_common(**kwargs))

    @converts(pydantic.EmailStr)
    def conv_pydantic_email(self, *args: Any, **kwargs: Any) -> BaseField:
        return EmailField(**self._standard_type_common(**kwargs))

    @converts(pydantic.AnyUrl)
    def conv_pydantic_url(self, *args: Any, **kwargs: Any) -> BaseField:
        return URLField(**self._standard_type_common(**kwargs))
