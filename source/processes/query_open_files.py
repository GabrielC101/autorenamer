#!/usr/bin/env python2.7
#
# Copyright (C) 2016 Gabriel R. Curio
#
# This file is part of Autorenamer.
#
# Autorenamer can not be copied and/or distributed without the express permission of Gabriel R. Curio
#
#
# All rights reserved.


import psutil


def get_files_open_iter():

    for proc in psutil.process_iter():

        try:
            flist = proc.open_files()

            if flist:

                for nt in flist:
                    yield (nt.path)

        except:
            pass


def open_files_containing_string(string_to_check):

    files_open_gen = get_files_open_iter()

    files_open = list(files_open_gen)

    files_open.sort()

    for open_file in files_open:
        if string_to_check in open_file:
            yield open_file


def is_file_path_open(file_path):

    files_open_gen = get_files_open_iter()

    for f in files_open_gen:

        if file_path == f:
            return True

    return False

