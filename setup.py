import setuptools
with open('README.rst') as f:
    ld = f.read()
setuptools.setup(
    name = 'relationlist',
    version = '1.1.0',
    author = 'wyz23x2',
    author_email = 'wyz23x2@163.com',
    description = 'A module that contains a class that supports relations.',
    long_description = ld,
    packages = setuptools.find_packages(),
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 6 - Mature",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
    
