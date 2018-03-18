from setuptools import setup, find_packages


def empty_local(version):
    return ''


setup(
    name='nesdict',
    use_scm_version={'local_scheme': empty_local},
    description='Support for xpath-like lookups in nested Python dicts.',
    long_description=open('README.md').read(),
    url='https://github.com/steersbob/nesdict',
    download_url='https://github.com/steersbob/nesdict/archive/0.1.tar.gz',
    author='Bob Steers',
    author_email='steers.bob@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
    extras_require={'dev': ['tox', 'pipenv']},
    setup_requires=['setuptools_scm'],
)
