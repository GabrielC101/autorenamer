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

def analyze_files_in_dir(dir):
    file_list = os.listdir(dir)
    file_list = [os.path.join(dir, f) for f in file_list]
    file_dict = {}
    for f in file_list:
        f_obj = FilePath(f)
        name = f_obj.file_name
        inode_num_m = str(f_obj.inode_num)
        file_dict[inode_num_m] = name
    return file_dict


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
        '''Renames file. Some programs change a files name after it is downloaded. Therefore, it is not acceptable
        to rely on the file name provided by inotify. This method checks to find the file's new name using the
        os module.'''

        inode_num = str(inotify_event.file.inode_num)

        # find watched directory
        a_dict = get_created_file(inode_num)
        watched_dir = a_dict['watched_dir']
        time_string = a_dict['time_string']

        file_dict = analyze_files_in_dir(watched_dir)


        # change file name
        current_file_name = file_dict[inode_num]
        from_path = os.path.join(watched_dir, current_file_name)
        to_path = os.path.join(watched_dir, time_string + '_'+ current_file_name)
        os.rename(from_path, to_path)


def main(folder_to_monitor):
    fm = Renamer(folder_to_monitor)


if __name__ == '__main__':

    main(sys.argv[1])
