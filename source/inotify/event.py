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

import datetime

from twisted.python.filepath import FilePath
from inotify_mask import InotifyMask




class InotifyEvent(object):
    def __init__(self, mask, file_changed, watch_path):
        self.mask = InotifyMask(mask)
        self.file_changed = FilePath(file_changed)
        self.watch_path = FilePath(watch_path)
        self.time = datetime.datetime.now()