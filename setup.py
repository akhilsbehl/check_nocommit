from setuptools import setup, find_packages

setup(
    name='check_nocommit',
    version='0.1.0',
    description='A pre-commit hook to check for #NOCOMMIT in python and bash files.',
    author='Akhil Behl',
    author_email='akhilsbehl@gmail.com',
    url='https://github.com/akhilsbehl/check_nocommit',
    packages=find_packages(),
    install_requires=[
        'gitpython',
        'pre-commit',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
