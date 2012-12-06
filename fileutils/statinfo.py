import os
import sys

class StatInfo:
    def __init__(self):
        self.platform = sys.platform
        self.st_common_stat = {}
        self.st_uncommon_stat = {}
        self.statinfo = None

    def populate_stat(self):
        """
        Populate statinfo into a dict
        """
        if self.statinfo is None:
            raise IOError("Stat information not available at input")

        self.st_common_stat = {
            'st_mode': statinfo.st_mode,
            'st_ino': statinfo.st_ino,
            'st_dev': statinfo.st_dev,
            'st_nlink': statinfo.st_nlink,
            'st_uid': statinfo.st_uid,
            'st_gid': statinfo.st_gid,
            'st_size': statinfo.st_size,
            'st_atime': statinfo.st_atime,
            'st_mtime': statinfo.st_mtime,
            'st_ctime': statinfo.st_ctime,
            'st_blocks': statinfo.st_blocks,
            'st_blksize': statinfo.st_blksize,
            'st_rdev': statinfo.st_rdev
            }
        # Platform specific stat information
        if self.platform == 'darwin':
            self.st_uncommon_stat = {
                'st_birthtime': statinfo.st_rsize,
                'st_flags': statinfo.st_flags,
                'st_gen': statinfo.st_flags
                }

    @classmethod
    def get_stat(cls, fd):
        if not isinstance(fd, int):
            raise ValueError('Invalid `fd` detected, integer value expected')
        cls.statinfo = os.fstat(fd)
        cls.populate_stat()
