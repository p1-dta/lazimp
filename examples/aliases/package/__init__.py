import lazimp

am: lazimp.ModuleType

__getattr__ = lazimp.lazy_import(
    aliases={'am': 'alias_module'},
    alias_module='package',
)
