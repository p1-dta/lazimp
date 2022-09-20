# Examples

You can find examples of how to use the library here.

## Project description

This example is the example from project description you can find here:
[LazImp README.md](https://github.com/Vikka/lazimp#readme).

Example
folder: [lazimp/examples/first_case](https://github.com/Vikka/lazimp/examples/basic)

In this example, the `heavy_module.py` is loaded only when you access the
package attribute named `heavy_module`. Before that, any code written in
`heavy_module.py` is not executed. Same for the `math` module.

## Aliases lazy loading

This example shows how to use aliases to lazy load modules.

Example
folder: [lazimp/examples/aliases](https://github.com/Vikka/lazimp/examples/aliasses)

In this example, the `alias_module.py` is loaded though the `am` alias.

## Bare sub import

This example shows how to use bare import to import packages and submodules at
once.

Example
folder: [lazimp/examples/bare_sub_import](https://github.com/Vikka/lazimp/examples/bare_sub_import)

In this example, `package_2.bare_sub_module_<1, 2, 3>` are loaded when you
use `package.package_2`.

## Benchmark

This example shows the difference between an import of `keras` and `aiohttp`
and a lazy import, with and without usage.

Example
folder: [lazimp/examples/benchmark](https://github.com/Vikka/lazimp/examples/benchmark)


With `lazimp`, no overhead is felt, and the import time only happen when you
use `keras` and `aiohttp` modules.