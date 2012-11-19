# -*- coding: utf-8 -*-
from fileutils.mime import mime_type

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

class FILE(object):

    """

    Bungee plugin to pull in FILE Metainformation across various different
    filetypes ranging from audio, video, documents, html formats. This class
    also provides extensive information extraction other than just Filesystem
    metainformation understanding specific use cases for each filetypes.

    """

    def __init__ (self):
        self.__file_type = None

    @classmethod
    def meta(cls, fd):
        ## TODO
        self.__file_type = mime_type(fd)
