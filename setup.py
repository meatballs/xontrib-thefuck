from setuptools import setup

setup(
    name='xontrib-thefuck',
    version='0.1',
    author='Owen Campbell',
    description="Xonsh extension for thefuck",
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    install_requires=['thefuck'],
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)
