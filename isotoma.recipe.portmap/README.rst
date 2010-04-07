Portmap buildout recipe
=======================

This package provides a buildout_ recipe to calculate TCP port offsets.  This
is useful when you are installing a stack of software, with multiple parts
needing TCP port numbers.

The calculated values are provided as buildout parameters in the section for
which this is the recipe.

.. _buildout: http://pypi.python.org/pypi/zc.buildout

For example::

    [ports]
    recipe = isotoma.recipe.portmap
    base = 8080
    offsets = 
        foo 0
        bar 1

    [baz]
    recipe = build.me.a.foo
    port = ${ports:foo}

    [qux]
    recipe = a.bar.if.you.please
    listen = tcp:${ports:bar}

This recipe will also produce an "INI file" called portmap.txt in the parts
directory, which is useful for reference if nothing else.

Mandatory parameters
--------------------

base
    The base port to calculate offsets from
offsets
    The map of names to offsets

License
-------

Copyright 2010 Isotoma Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


