import lazimp

sub_package: lazimp.ModuleType

__getattr__ = lazimp.lazy_import('package_2.bare_sub_module',
                                 'package_2.bare_sub_module_2')
