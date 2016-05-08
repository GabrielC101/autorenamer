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


def get_files_open():
    for proc in psutil.process_iter():
        try:
            flist = proc.open_files()
            if flist:
                #print(proc.pid,proc.name)
                for nt in flist:
                    yield (nt.path)

        # This catches a race condition where a process ends
        # before we can examine its files
        except psutil.NoSuchProcess as err:
            #print("****")
            pass
