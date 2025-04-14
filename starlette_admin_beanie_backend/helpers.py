import typing as t

from beanie import Document
from beanie.odm.operators.find import comparison as c, evaluation as e, logical as l


def normalize_list(
        arr: t.Optional[t.Sequence[t.Any]], is_default_sort_list: bool = False
) -> t.Optional[t.Sequence[str]]:
    if arr is None:
        return None
    _new_list = []
    for v in arr:
        if isinstance(v, str):
            _new_list.append(v)
        elif (
                isinstance(v, tuple) and is_default_sort_list
        ):  # Support for fields_default_sort:
            if len(v) == 2 and isinstance(v[0], str) and isinstance(v[1], bool):
                _new_list.append((v[0], v[1]))
            else:
                raise ValueError(
                    "Invalid argument, Expected Tuple[str, bool]"
                )
        else:
            raise ValueError(f"Expected str, got {type(v).__name__}")
    return _new_list


def resolve_deep_query(
        where: t.Dict[str, t.Any],
        model: t.Type[Document],
        logic=None
) -> t.Any:
    queries = []
    if isinstance(where, list):
        for item in where:
            queries.append(resolve_deep_query(item, model))
    else:
        for k, v in where.items():
            if k == "and":
                queries = resolve_deep_query(v, model, k)
            elif k == "or":
                queries = resolve_deep_query(v, model, k)
            else:
                for op, val in v.items():
                    match op:
                        case "eq":
                            return c.Eq(k, val)
                        case "neq":
                            return c.NE(k, val)
                        case "lt":
                            return c.LT(k, val)
                        case "gt":
                            return c.GT(k, val)
                        case "le":
                            return c.LTE(k, val)
                        case "ge":
                            return c.GTE(k, val)
                        case "in":
                            return c.In(k, val)
                        case "not_in":
                            return c.NotIn(k, val)
                        case "startswith":
                            return e.RegEx(k, rf"^{val}", "i")
                        case "not_startswith":
                            return l.Nor(e.RegEx(k, rf"^{val}"))
                        case "endswith":
                            return e.RegEx(k, rf"{val}$")
                        case "not_endswith":
                            return l.Nor(e.RegEx(k, rf"{val}$"))
                        case "contains":
                            return e.RegEx(k, rf"{val}")
                        case "not_contains":
                            return l.Nor(e.RegEx(k, rf"{val}"))
                        case "is_false":
                            return c.Eq(k, False)
                        case "is_true":
                            return c.Eq(k, True)
                        case "is_null":
                            return c.Eq(k, None)
                        case "is_not_null":
                            return c.NE(k, None)
                        case "between":
                            return l.And(k >= val[0], k <= val[1])
                        case "not_between":
                            return l.And(k < val[0], k > val[1])
    if logic:
        if logic == "or":
            return {"$or": queries}
        else:
            return {"$and": queries}
    return queries
