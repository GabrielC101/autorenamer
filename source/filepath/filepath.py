import os
import mimetypes

class Filepath(object):


    def __init__(self, string=''):
        self._string = os.path.abspath(string)





    @property
    def absolute_path(self):
        return os.path.abspath(self._string)


    @property
    def file_name(self):
        return os.path.basename(self._string)


    @classmethod
    def common_prefix(cls, list):
        return os.path.commonprefix(list)


    @property
    def parent_directory(self):
        return Filepath(os.path.dirname(self._string))


    @property
    def exists(self):
        return os.path.exists(self._string)

    @property
    def is_broken_sym_link(self):
        if os.path.lexists(self._string) and not os.path.exists(self._string):
            return os.path.basename(self._string)


    @property
    def is_file(self):
        return os.path.isfile(self._string)


    @property
    def is_directory(self):
        return os.path.isdir(self._string)


    @property
    def is_sym_link(self):
        return os.path.islink(self._string)


    @property
    def is_mount_point(self):
        return os.path.ismount(self._string)

    @property
    def real_path(self):
        return Filepath(os.path.realpath(self._string))


    @property
    def _stat(self):
        return os.stat(self._string)

    @property
    def inode_num(self):
        return self._stat.st_ino

    @property
    def mode(self):
        return self._stat.st_mode

    @property
    def dev(self):
        return self._stat.st_dev


    @property
    def nlink(self):
        return self._stat.st_nlink


    @property
    def uid(self):
        return self._stat.st_uid


    @property
    def gid(self):
        return self._stat.st_gid


    @property
    def size(self):
        return self._stat.st_size


    @property
    def atime(self):
        return self._stat.st_atime


    @property
    def mtime(self):
        return self._stat.st_mtime


    @property
    def ctime(self):
        return self._stat.st_ctime



    @property
    def fields(self):
        return self._stat.n_fields


    @property
    def sequence_fields(self):
        return self._stat.n_sequence_fields


    @property
    def unnamed_fields(self):
        return self._stat.n_unnamed_fields


    @property
    def file_name_base(self):
        path, ext = os.path.splitext(self._string)
        if '/' in path:
            return path.split('/')[-1]
        else:
            return path

    @property
    def file_name_extension(self):
        path, ext = os.path.splitext(self._string)
        return ext

    @property
    def mime_type(self):
        return mimetypes.guess_type(self._string, strict=False)[0]


    @property
    def mime_encoding(self):
        return mimetypes.guess_type(self._string, strict=False)[1]


    @classmethod
    def expand_user_dir(cls, string):
        return os.path.expanduser(string)


    def __repr__(self):
        return '<Filepath object: %s>' % self._string
    '''

    class Mime(object):
        def __init__(self, path):
            self._mimetypes = mimetypes(path)

            @property
            def type(self):
                return self._mimetypes[0]

            @property
            def encoding(self):
                return self._mimetypes[1]
    '''