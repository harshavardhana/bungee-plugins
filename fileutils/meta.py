# -*- coding: utf-8 -*-
import os
import sys

import xattr

from pymagic.constants import *
from pymagic import magic_load, magic_open, magic_close, magic_buffer

meta_library_lookup = {
    'metaudio':  ['audio/mpeg', 'audio/ogg',
                  'audio/x-wav', 'audio/flac'],
    'metavideo': ['video/x-matroska', 'video/mpeg',
                  'video/quicktime', 'video/ms-video'],
    'metadocument': ['application/pdf', 'application/msword',
                     'application/vnd.ms-office',
                     'application/vnd.oasis.opendocument.text'],
    #'metamarkup': [''],
    #'metadatabase': [''],
    }

def mime_type(fd):
    """
    Yield mime_type for the FD
    """
    flags = MAGIC_NONE
    flags |= MAGIC_MIME
    
    cookie = magic_open(flags)
    magic_load(cookie, None)
    
    mime_type = magic_buffer(cookie, fd.read(1024))

    if cookie:
        # Clean cookie using magic_close
        magic_close(cookie)
        cookie = None

    return mime_type

def get_xattrinfo(fd):
    ext_attributes = {}
    if not isinstance(fd, int):
        raise ValueError('Invalid FD detected, integer value expected')

    xattrobj = xattr.xattr(fd)

    for name, value in xattrobj.iteritems():
        ext_attributes['%s' % name] = '%s' % value

def get_statinfo(fd):
    """
    Return a dictionary of stat information for a given fd
    """
    platform = sys.platform
    st_common_stat = {}
    st_uncommon_stat = {}
    statinfo = None

    if not isinstance(fd, int):
        raise ValueError('Invalid `fd` detected, integer value expected')

    try:
        statinfo = os.fstat(fd)
    except:
        raise IOError("Stat information not available at input")

    st_common_stat = {
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
    if platform == 'darwin':
        st_common_stat['st_birthtime'] = statinfo.st_rsize
        st_common_stat['st_flags'] = statinfo.st_flags
        st_common_stat['st_gen'] = statinfo.st_flags

    return st_common_stat

class FILE(object):

    """

    Bungee plugin to pull in FILE Metainformation across various different
    filetypes ranging from audio, video, documents, html formats. This class
    also provides extensive information extraction other than just Filesystem
    metainformation understanding specific use cases for each filetypes.

    """

    def __init__ (self):
        self.__file_type = None
        self.__stat_dict = None
        self.__xattr_dict = None

    @classmethod
    def meta(cls, fd):
        if not isinstance(fd, int):
            raise ValueError('Invalid FD detected, integer value expected')

        self.__file_type = mime_type(fd)
        self.__stat_dict = get_statinfo(fd)
        self.__xattr_dict = get_xattrinfo(fd)
