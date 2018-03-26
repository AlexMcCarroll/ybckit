"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/yuantiku/ybckit
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ybckit',  # Required

    version='0.0.4',

    description='Python library kit for education with yuanfudao.',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/yuantiku/ybckit',

    author='Yuchen <pw> Zhang',

    author_email='zhangyc@fenbi.com',

    # classifiers=[
        # # How mature is this project? Common values are
        # #   3 - Alpha
        # #   4 - Beta
        # #   5 - Production/Stable
        # 'Development Status :: 3 - Alpha',
        # 'Intended Audience :: Students',
        # 'Topic :: Software Development :: Build Tools',
        # 'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.6',
    # ],

    keywords='yuanfudao gui media kit',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    install_requires=['easygui'],  # Optional

    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={  # Optional
        'console_scripts': [
            'ybckit=ybckit:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/yuantiku/ybckit/issues',
        'Source': 'https://github.com/yuantiku/ybckit/',
    },
)
