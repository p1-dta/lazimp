import collections.abc

from types import ModuleType


def lazy_import(
        *bare_imports: str,
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

    :param bare_imports: Any number of module names to import.
    :param aliases: A mapping of alias names to module names.
    :param sub_import: A mapping of module names to package names.
    :param kw_sub_import: Keyword arguments of module names to package names.
    :return: A function that returns the imported modules.
    """
    if aliases is None:
        aliases = {}
    if sub_import is None:
        sub_import = {}

    imports = {name for name in bare_imports if len(name.split('.')) == 1}
    top_level_import = collections.defaultdict(list)
    for import_path in bare_imports:
        root, *path = (import_path.split('.'))
        if path:
            top_level_import[root].append(import_path)

    sub_import.update(kw_sub_import)

    import functools
    import importlib

    @functools.cache
    def getattr_(name: str) -> ModuleType:
        name = aliases.get(name, name)

        if name in imports:
            try:
                return importlib.import_module(name)
            except ModuleNotFoundError as e:
                raise ModuleNotFoundError(
                    f'Module has no attribute {name!r}'
                ) from e

        if name in sub_import:
            try:
                return importlib.import_module(f'.{name}', sub_import[name])
            except ModuleNotFoundError as e:
                raise AttributeError(
                    f'Module has no attribute {name!r}') from e

        if name in top_level_import:
            try:
                module = importlib.__import__(top_level_import[name].pop())
                for import_path_ in top_level_import[name]:
                    module = importlib.__import__(import_path_)
                return module
            except ModuleNotFoundError as e:
                raise AttributeError(
                    f'Module has no attribute {name!r}') from e

        raise AttributeError(f'Module has no attribute {name!r}')

    return getattr_
