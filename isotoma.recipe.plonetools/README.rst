Introduction
============

This recipe enables you to create and update a Plone site as part of a buildout run.  This recipe only aims to run profiles and Quickinstall products.  It is assumed that the install methods, setuphandlers, upgrade steps, and other recipes will handle the rest of the work.

NOTE: There is a friendly fork of http://pypi.python.org/pypi/collective.recipe.plonesite

Options
=======

.. [1] Profiles have the following format: ``<package_name>:<profile>`` (e.g. ``my.package:default``).  The profile can also be prepended with the ``profile-`` if you so choose (e.g. ``profile-my.package:default``).

.. [2] The product name is typically **not** the package name such as `Products.MyProduct`, but just the product name `MyProduct`. Quickest way to find out the name that is expected is to 'inspect' the Quickinstaller page and see what value it is passing in.

site-id
    The id of the Plone site that the script will create.  This will also be used to update the site once created.  Default: Plone

admin-user
    The id of an admin user that will be used as the 'Manager'.  Default: admin

products-initial
    A list of products to quickinstall just after initial site creation. See above for information about the product name format [2]_.

profiles-inital
    A list of GenericSetup profiles to run just after initial site creation. See above for informaion on the expected profile id format [1]_.

products
    A list of products to quickinstall each time buildout is run. See above for information about the product name format [2]_.

profiles
    A list of GenericSetup profiles to run each time buildout is run. See above for informaion on the expected profile id format [1]_.

instance
    The name of the instance that will run the script. Default: instance

zeoserver
    The name of the zeoserver part that should be used.  This is only required if you are using a zope/zeo setup. Default: not set

before-install
    A system command to execute before installing Plone.  Optional.  You could use this to start a Supervisor daemon to launch ZEO, instead of launching ZEO directly.  You can use this option in place of the zeoserver option.

after-install
    A system command to execute after installing Plone.  Optional.

site-replace
    Replace any existing plone site named site-id. Default: false

enabled
    Option to start up the instance/zeoserver.  Default: true.  This can be a useful option from the command line if you do not want to start up Zope, but still want to run the complete buildout.
    
    $ bin/buildout -Nv plonesite:enabled=false

pre-extras
    An absolute path to a file with python code that will be evaluated before running Quickinstaller and GenericSetup profiles.  Multiple files can be given.  Two variables will be available to you.  The app variable is the zope root.  The portal variable is the plone site as defined by the site-id option. NOTE: file path cannot contain spaces. Default: not set

post-extras
    An absolute path to a file with python code that will be evaluated after running Quickinstaller and GenericSetup profiles.  Multiple files can be given.  Two variables will be available to you.  The app variable is the zope root.  The portal variable is the plone site as defined by the site-id option. NOTE: file path cannot contain spaces. Default: not set

