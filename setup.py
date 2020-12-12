import setuptools
setuptools.setup(
    name = 'relationlist',
    version = '2.0.0b1',
    author = 'wyz23x2',
    author_email = 'wyz23x2@163.com',
    description = 'A module that contains a class that supports relations.',
    long_description = '''See `the official documentation <https://relationlist.readthedocs.io>`_\ .''',
    packages = setuptools.find_packages(),
    install_requires=['green>=3.2'],
    python_requires='>=3.8, !=3.9.0b2',
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8", # NOTE: 8 support will be dropped in v2.3.
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
    
