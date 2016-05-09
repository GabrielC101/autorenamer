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
from __future__ import absolute_import

import os
import sys


from inotifers.monitor import InotifyFileMonitorBase
from autorenamer.filepath import FilePath
from autorenamer.persistence.set_directory import initialize_autorenamer_dir
from autorenamer.persistence.data_file import store_created_file
from autorenamer.persistence.data_file import get_created_file


def get_time_string(time_obj):
    time_string = str(time_obj.year) + '-' + \
    str(time_obj.month) + '-' + \
    str(time_obj.day) + '_' + \
    str(time_obj.hour) + '-' + \
    str(time_obj.minute) + '-' + \
    str(time_obj.second)

    return time_string


class Renamer(InotifyFileMonitorBase):

    def __init__(self, initial_watch_path='.'):
        super(Renamer, self).__init__(initial_watch_path)
        initialize_autorenamer_dir()

    def on_IN_CREATE(self, inotify_event):
        inode_num = inotify_event.file.inode_num
        created_path = inotify_event.file.absolute_path

        time_string = get_time_string(inotify_event.time)
        watched_dir_obj = inotify_event.file.parent_directory
        watched_dir = watched_dir_obj.absolute_path
        store_created_file(inode_num, created_path, time_string, watched_dir)

    def on_IN_CLOSE_WRITE(self, inotify_event):
        print 'close write'
        inode_num = str(inotify_event.file.inode_num)
        print inode_num
        a_dict = get_created_file(inode_num)
        print a_dict
        watched_dir = a_dict['watched_dir']
        print watched_dir
        file_list = os.listdir(watched_dir)
        file_list = [os.path.join(watched_dir, f) for f in file_list]
        print file_list
        file_dict = {}
        for f in file_list:
            f_obj = FilePath(f)
            name = f_obj.file_name
            inode_num_m = str(f_obj.inode_num)
            print type(inode_num_m)
            print type (name)
            file_dict[inode_num_m] = name
        print file_dict

        file_name = file_dict[inode_num]
        from_path = os.path.join(watched_dir, file_name)
        to_path = os.path.join(watched_dir, a_dict['time_string'] + '_'+ file_name)
        print from_path
        print to_path
        os.rename(from_path, to_path)


def main(folder_to_monitor):
    fm = Renamer(folder_to_monitor)


if __name__ == '__main__':

    main(sys.argv[1])
