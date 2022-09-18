import collections.abc

# noinspection PyUnresolvedReferences
from types import ModuleType


def lazy_import(
        bare_import: collections.abc.Container | None = None,
        sub_import: collections.abc.Mapping[str, str | None] | None = None,
        aliases: collections.abc.Mapping[str, str] | None = None,
):
    if bare_import is None:
        bare_import = set()
    if sub_import is None:
        sub_import = {}
    if aliases is None:
        aliases = {}

    import functools
    import importlib

    @functools.cache
    def getattr_(name: str):
        name = aliases.get(name, name)

        if name not in bare_import and name not in sub_import:
            raise AttributeError(
                f'Module has no attribute {name!r}'
            ) from None

        if name in bare_import:
            try:
                return importlib.import_module(name)
            except ModuleNotFoundError as e:
                raise ModuleNotFoundError(
                    f'Module has no attribute {name!r}'
                ) from e

        try:
            return importlib.import_module(f'.{name}',
                                           sub_import[name])
        except ModuleNotFoundError as e:
            raise AttributeError(f'Module has no attribute {name!r}') from e

    return getattr_
