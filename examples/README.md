# Examples

You can find examples of how to use the library here.

## First case: Project description example

This example is just the example from project description you can find here:
[LazImp README.md](https://github.com/Vikka/lazimp#readme).

Project
folder: [lazimp/examples/first_case](https://github.com/Vikka/lazimp/examples/first_case)

In this example, only the `heavy_module.py` is loaded, only when you access the
package attribute named `heavy_module`. Before that, any code written in
`heavy_module.py` is not executed.

## Aliases lazy loading

This example shows how to use aliases to lazy load modules.

Example
folder: [lazimp/examples/aliases](https://github.com/Vikka/lazimp/examples/aliasses)

In this example, the `alias_module.py` is loaded though the `am` alias.
