#from distutils.core import setup
from setuptools import setup
import pypandoc
import os


readme_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')
long_desc = pypandoc.convert('README.md', 'rst')
version='1.0.1'

setup(
    name='usexif',
    packages=['usexif'],
    version=version,
    description='get geo data and taken date',
    long_description=long_desc,
    author='Juncheol Cho',
    author_email='zironycho@gmail.com',
    url='https://github.com/zironycho/usexif',
    download_url='https://github.com/zironycho/usexif/tarball/{}'.format(version),
    keywords=['exif', 'geo', 'taken', 'geo', 'geographic coordinate', 'coordinate'],
    license='MIT',
    classifiers=[],
    install_requires=[
       'exifread>=2.1.2'
    ],
)
