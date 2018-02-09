from setuptools import setup, find_packages


setup(
    name='xdict',
    version='0.1',
    description='Support for xpath-like lookups in nested Python dicts.',
    long_description=open('README.md').read(),
    url='https://github.com/Kargathia/xdict',
    download_url='https://github.com/Kargathia/xdict/archive/0.1.tar.gz',
    author='Bob Steers',
    author_email='kargathia@hotmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='xpath dicts nested lookup',
    packages=find_packages(exclude=['tests']),
    install_requires=['dpath'],
    extras_require={'dev': ['tox']}
)
