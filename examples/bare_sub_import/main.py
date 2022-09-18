import package

print('Before access to package_2')
print('load of bare_sub_module and bare_sub_module_2: ', package.package_2)
print('After access to package_2')
print('package_2.bare_sub_module: ', package.package_2.bare_sub_module)
print('package_2.bare_sub_module_2: ',
      package.package_2.bare_sub_module_2)
print(
    'package_2.bare_sub_module_3 access success because package_2 expose it: ',
    package.package_2.bare_sub_module_3)
print(
    'package_2.bare_sub_module_4 access failed because package_2 does not '
    'expose it: ', package.package_2.bare_sub_module_4)
