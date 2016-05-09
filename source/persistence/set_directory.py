import os
from os.path import expanduser




def make_autorenamer_dir():
    a_path = get_autorenamer_dir()
    os.mkdir(a_path)

def get_autorenamer_dir():
    home = expanduser('~')
    autorenamer_path = os.path.join(home, '.local/share/autorenamer')
    return autorenamer_path

def autorenamer_dir_exists():
    a_path = get_autorenamer_dir()
    return os.path.exists(a_path)

def initialize_autorenamer_dir():
    if not autorenamer_dir_exists():
        make_autorenamer_dir()






