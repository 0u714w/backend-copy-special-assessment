#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/




__author__ = "dougenas"


import re
import os
import shutil
import subprocess
import argparse
import sys


__author__ = "dougenas"


def get_special_paths(dir):
    special_paths = []
    files = os.listdir(dir)
    for file in files:
        if re.search(r'__\w+__', file):
            special_paths.append(file)
    return special_paths


def copy_to(paths, dir):
    print('copy_to', paths, dir)


def zip_to(paths, zippath):
    print('zip_to', paths, zippath)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='src dir to look for local files')
    args = parser.parse_args()

    print(args)

    if not args.todir and not args.tozip:
        for file in get_special_paths(args.fromdir):
            print(os.path.abspath(file))


if __name__ == "__main__":
    main()
