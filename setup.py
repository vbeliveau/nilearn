#! /usr/bin/env python

descr = """A set of python modules for neuroimaging..."""

import sys
import os

from setuptools import setup, find_packages


# Make sources available using relative paths from this file's directory.
#  dirname can return '', so use 'or' below to avoid chdir on empty
#  while being succinct.
os.chdir(os.path.dirname(__file__) or os.getcwd())


def load_version():
    """Returns the version found in nilearn/version.py

    Importing nilearn is not an option because there may dependencies
    like nibabel which are not installed and setup.py is supposed to
    install them.
    """
    # load all vars into globals, otherwise
    #   the later function call using global vars doesn't work.
    globals_dict = {}
    execfile(os.path.join('nilearn', 'version.py'), globals_dict)

    return globals_dict

def is_installing():
    return len(sys.argv) > 1 and sys.argv[1] == 'install'


_VERSION_GLOBALS = load_version()
DISTNAME = 'nilearn'
DESCRIPTION = 'Statistical learning for neuroimaging in Python'
LONG_DESCRIPTION = open('README.rst').read()
MAINTAINER = 'Gael Varoquaux'
MAINTAINER_EMAIL = 'gael.varoquaux@normalesup.org'
URL = 'http://nilearn.github.com'
LICENSE = 'new BSD'
DOWNLOAD_URL = 'http://nilearn.github.com'
VERSION = _VERSION_GLOBALS['__version__']


if __name__ == "__main__":
    if is_installing():
        eval('_check_module_dependencies(manual_install_only=True)', _VERSION_GLOBALS)

    old_path = os.getcwd()
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(local_path)
    sys.path.insert(0, local_path)

    # Convert module metadata into list of {mod_name}>={minver}
    #   as required by install_requires
    formatted_dependencies = ['%s>=%s' % (mod, meta['minver'])
        for mod, meta in _VERSION_GLOBALS['REQUIRED_MODULE_METADATA']
        if not meta['manual_install']]

    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: C',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
          ],
          packages=find_packages(),
          package_data={'nilearn.data': ['*.nii.gz'],
                        'nilearn.plotting.glass_brain_files': ['*.json'],
                        'nilearn.tests.data': ['*']},
          install_requires=formatted_dependencies,
    )
