from setuptools import setup, find_packages

version = '0.0.0'

setup(
    name = 'isotoma.recipe.portmap',
    version = version,
    description = "Simple way of configuring port numbers as offsets from a base, for use in buildout scripts.",
    long_description = open("README.rst").read() + "\n" + \
                       open("CHANGES.txt").read(),
    classifiers = [
        "Framework :: Buildout",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords = "buildout",
    author = "Doug Winter",
    author_email = "doug.winter@isotoma.com",
    license="Apache Software License",
    packages = find_packages(exclude=['ez_setup']),
    package_data = {
        '': ['README.rst', 'CHANGES.txt'],
    },
    namespace_packages = ['isotoma', 'isotoma.recipe'],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'zc.buildout',
    ],
    entry_points = {
        "zc.buildout": [
            "default = isotoma.recipe.portmap:Portmap",
        ],
    }
)
