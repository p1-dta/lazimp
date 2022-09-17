# LazImp

LazImp is a package that allows lazy loading of python modules, packages and
symboles for python 3.10+. This package allows you to load modules and packages
only **when** the user use it. From dynamic import to "I only need this
function, not the whole framework", the start-up time is speed-up and delayed
over the execution of the software.

## Example

First, you may have long loading or memory heavy modules to expose in your
package api:

```python
# heavy_module.py
from time import sleep

sleep(10)
print('heavy_module loaded')
```

But instead of importing them directly, you can do a lazy import in
the `__init__.py`:

```python
# __init__.py of a package
import lazimp

heavy_module: lazimp.ModuleType

__getattr__ = lazimp.lazy_import({'heavy_module'})
```

Now, when you import the package:

```python
# main.py
import package

print('Before access to heavy_module')
print(package.heavy_module)
print('After access to heavy_module')
```

And the output:

```txt
Before access to heavy_module
(wait 10 sec)
heavy_module loaded
<module 'heavy_module' from '...'>
After access to heavy_module
```

Without the lazy loading of `heavy_module.py`, the output would have been:

```txt
(wait 10 sec)
heavy_module loaded
Before access to heavy_module
<module 'heavy_module' from '...'>
After access to heavy_module
```
