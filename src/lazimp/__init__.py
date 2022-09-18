import collections.abc

# noinspection PyUnresolvedReferences
from types import ModuleType


def lazy_import(
        bare_import: collections.abc.Container | None = None,
        sub_import: collections.abc.Mapping[str, str | None] | None = None,
):
    if bare_import is None:
        bare_import = set()
    if sub_import is None:
        sub_import = {}

    import functools
    import importlib

    @functools.cache
    def getattr_(name: str):
        if name not in bare_import and name not in sub_import:
            raise AttributeError(
                f'module {__name__!r} has no attribute {name!r}'
            ) from None

        try:
            return importlib.import_module(f'.{name}',
                                           sub_import.get(name, ''))
        except ModuleNotFoundError:
            raise AttributeError(
                f'module {__name__!r} has no attribute {name!r}'
            ) from None

    return getattr_
