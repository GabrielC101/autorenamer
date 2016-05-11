import pickle
import os

from autorenamer.persistence.set_directory import get_autorenamer_dir



def store_created_file(inode_num, created_path, time_string, watched_dir):
    a_path = get_autorenamer_dir()
    d_path = os.path.join(a_path, str(inode_num))

    try:
        os.remove(d_path)
    except OSError:
        pass

    a_dict = {
        'inode_num': inode_num, 'created_path': created_path, 'time_string': time_string, \
        'watched_dir':watched_dir, 'appended':False
    }

    pickle.dump(a_dict, open(d_path,'wb'))

def get_created_file(inode_num):
    a_path = get_autorenamer_dir()
    d_path = os.path.join(a_path, str(inode_num))
    a_dict = pickle.load(open(d_path,'rb'))
    return a_dict

