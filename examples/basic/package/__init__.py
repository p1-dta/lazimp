import lazimp

math: lazimp.ModuleType
heavy_module: lazimp.ModuleType

# __getattr__ = lazimp.lazy_import('math', 'package.heavy_module')
__getattr__ = lazimp.lazy_import(
    'math',
    heavy_module='package',
)
