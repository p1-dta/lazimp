import lazimp

am: lazimp.ModuleType

__getattr__ = lazimp.lazy_import(
    sub_import={'alias_module': 'package'},
    aliases={'am': 'alias_module'}
)
