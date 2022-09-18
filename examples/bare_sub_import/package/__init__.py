import lazimp

package_2: lazimp.ModuleType

__getattr__ = lazimp.lazy_import('package_2.bare_sub_module',
                                 'package_2.bare_sub_module_2')
