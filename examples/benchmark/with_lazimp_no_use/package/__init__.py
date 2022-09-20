import lazimp

keras: lazimp.ModuleType
aiohttp: lazimp.ModuleType

__getattr__ = lazimp.lazy_import(
    'keras',
    'aiohttp',
)
