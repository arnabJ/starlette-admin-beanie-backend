from typing import Optional, Sequence

from starlette.middleware import Middleware
from starlette_admin.auth import BaseAuthProvider
from starlette_admin.base import BaseAdmin
from starlette_admin.i18n import I18nConfig
from starlette_admin.i18n import lazy_gettext as _
from starlette_admin.views import CustomView


class Admin(BaseAdmin):
    def __init__(
            self,
            title: str = _("Admin"),
            base_url: str = "/admin",
            route_name: str = "admin",
            logo_url: Optional[str] = None,
            login_logo_url: Optional[str] = None,
            templates_dir: str = "templates",
            statics_dir: Optional[str] = None,
            index_view: Optional[CustomView] = None,
            auth_provider: Optional[BaseAuthProvider] = None,
            middlewares: Optional[Sequence[Middleware]] = None,
            debug: bool = False,
            i18n_config: Optional[I18nConfig] = None,
            favicon_url: Optional[str] = None,
    ) -> None:
        super().__init__(
            title=title,
            base_url=base_url,
            route_name=route_name,
            logo_url=logo_url,
            login_logo_url=login_logo_url,
            templates_dir=templates_dir,
            statics_dir=statics_dir,
            index_view=index_view,
            auth_provider=auth_provider,
            middlewares=middlewares,
            debug=debug,
            i18n_config=i18n_config,
            favicon_url=favicon_url,
        )
