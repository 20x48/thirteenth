from setuptools import setup, find_packages

VERSION = open('thirteenth/ver.py', encoding='utf-8')
README = open('README.md', encoding='utf-8')

setup(
    name='thirteenth',
    author='20x48',
    author_email='the20x48@outlook.com',
    url='https://github.com/20x48/thirteenth',
    version=VERSION.readline()[15:-2],
    packages=find_packages(),
    project_urls={'Github': 'https://github.com/20x48/thirteenth'},
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description='"Flavored Datetime Converter"',
    long_description=README.read(),
    long_description_content_type='text/markdown'
)

VERSION.close()
README.close()