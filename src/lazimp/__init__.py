import collections.abc

from types import ModuleType


def lazy_import(
        *imports: str,
        aliases: collections.abc.Mapping[str, str] | None = None,
        sub_import: collections.abc.Mapping[str, str] | None = None,
        **kw_sub_import: str,
) -> collections.abc.Callable[[str], ModuleType]:
    """
    Lazily import modules.

    >>> lazy_import('package', 'package_2', 'package_3', ...)
    >>> lazy_import('package.submodule')  # fail ATM
    >>> lazy_import(submodule='package')
    >>> lazy_import(sub_import={'submodule':'package'})
    >>> lazy_import('module', aliases={'md': 'module'})
    >>> lazy_import(aliases={'smd': 'submodule'}, submodule='package')
    >>> lazy_import(
            'module',
            aliases={'md': 'module', 'smd': 'submodule'},
            submodule='package',
        )
    >>> lazy_import(
            'module',
            aliases={'md': 'module', 'smd': 'submodule', 'smd2': 'submodule2'},
            submodule='package',
            sub_import={'submodule2':'package'}
        )

    :param imports: Any number of module names to import.
    :param aliases: A mapping of alias names to module names.
    :param sub_import: A mapping of module names to package names.
    :param kw_sub_import: Keyword arguments of module names to package names.
    :return: A function that returns the imported modules.
    """
    imports = set(imports)
    if aliases is None:
        aliases = {}
    if sub_import is None:
        sub_import = {}
    sub_import = sub_import | kw_sub_import

    import functools
    import importlib

    @functools.cache
    def getattr_(name: str) -> ModuleType:
        name = aliases.get(name, name)

        if name not in imports and name not in sub_import:
            raise AttributeError(
                f'Module has no attribute {name!r}'
            ) from None

        if name in imports:
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
