#! /usr/bin/env python

# -*- coding: utf-8 -*-

# (c) 2017 Marcos Dione <mdione@grulic.org.ar>
# for licensing details see the file LICENSE.txt

from distutils.core import setup

setup(
    name ='objict',
    version = '0.1',
    description = 'Objecjs that behave like JavaScript objects.',
    author = 'Marcos Dione',
    author_email = 'mdione@grulic.org.ar',
    url = 'https://github.com/StyXman/objict',
    py_modules = [ 'objict' ],
    license = 'GPLv3',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        ],
    )
