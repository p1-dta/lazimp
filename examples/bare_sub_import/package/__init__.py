import lazimp

package_2: lazimp.ModuleType

__getattr__ = lazimp.lazy_import('package_2.bare_sub_module_1',
                                 'package_2.bare_sub_module_2')
