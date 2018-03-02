from setuptools import setup, find_packages


setup(
    name='nesdict',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    setup_requires=['setuptools-git-version'],
    description='Support for xpath-like lookups in nested Python dicts.',
    long_description=open('README.md').read(),
    url='https://github.com/Kargathia/nesdict',
    download_url='https://github.com/Kargathia/nesdict/archive/0.1.tar.gz',
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
