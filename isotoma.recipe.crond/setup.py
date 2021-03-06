from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name = 'isotoma.recipe.crond',
    version = version,
    description = "Buildout recipes for /etc/cron.d.",
    url = "http://pypi.python.org/pypi/isotoma.recipe.crond",
    long_description = open("README.rst").read() + "\n" + \
                       open("CHANGES.txt").read(),
    classifiers = [
        "Framework :: Buildout",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords = "buildout cron",
    author = "John Carr",
    author_email = "john.carr@isotoma.com",
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
            "default = isotoma.recipe.crond:Cron",
        ],
    }
)
