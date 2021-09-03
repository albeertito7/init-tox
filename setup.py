import sys, os
from setuptools import setup, find_packages

NAME = 'init-tox'
DESCRIPTION = 'Introduction to the tox automation tool and python packaging'
URL = 'https://github.com/albeertito7/init-tox'
EMAIL = 'albertperezdatsira@gmail.com'
AUTHOR = 'albeertito7'
VERSION = '0.1.0'
REQUIRES_PYTHON = '>=3.6.0'

REQUIRED = [] # required packages for this module to be executed
EXTRAS = {} # optional packages

# to work with absoulte paths
PATH = os.path.abspath(os.path.dirname(__file__))

# to extract the description from the README.md file
try:
    with open(os.path.join(PATH, "README.md"), 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "init-tox"

about = {}
if 'VERSION' not in locals() or not VERSION:
    try:
        with open(os.path.join(PATH, "src", "__version__.py")) as f:
            exec(f.read(), about)
    except FileNotFoundError:
        about['__version__'] = '0.1.0' # default version
else:
    about['__version__'] = VERSION

# where the magic happens:
setup(
    name='src',
    version=about['__version__'],
    description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # if your package is a single module, use this instead of 'packages':
    #py_modules=['mypackage']
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
    #scripts=[] #for scripts
)

"""
If is a long-term project, at some point
this setup.py will grow 
"""

"""
Some definitions:
    - package: folder / directory which contains the "__init__.py" file
    - module: valid python (.py) file
    - distribution: how one package gets related to other packages and modules

Example: let's say you want to install one package called "foo", then

$ git clone https://github.com/user/foo
$ cd foo
$ python setup.py install

in this way you will get installed the package "foo" on your active python environment
setting the "foo" content into the python/site-packages

but, if you prefer to use it but not completly install on your python env, then just do

$python setup.py develop

this will create symbolic links to the source folder, instead of copying all the stuff
Mainly this useful when treating with large packages
"""

"""
$ python setup.py register
$ python setup.py upload
$ python setup.py --sign upload
"""