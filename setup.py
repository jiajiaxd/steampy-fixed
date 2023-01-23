from setuptools import setup
import sys

if not sys.version_info[0] == 3 and sys.version_info[1] < 5:
    sys.exit('Python < 3.5 is not supported')

version = '2.1'

setup(
    name='steampy-fixed',
    packages=['steampy'],
    version=version,
    description='A Steam lib for trade automation(fixed)',
    author='jiajiaxd',
    author_email='i@jiajiaxd.com',
    license='MIT',
    url='https://github.com/jiajiaxd/steampy-fixed',
    download_url='https://github.com/jiajiaxd/steampy-fixed/tarball/' + version,
    keywords=['steam', 'trade', ],
    classifiers=[],
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rsa"
    ],
)
