import os
import sys

import ctypes
import ctypes.util

from ctypes import c_char_p, c_int, c_size_t, c_void_p

glfs_dll = ctypes.util.find_library("libglusterfs")
if glfs_dll:
    glfs = ctypes.CDLL(glfs_dll)

xdr_dll = ctypes.util.find_library("libgfxdr")
if xdr_dll:
    xdr = ctypes.CDLL(xdr_dll)

api_gfapi_dll = ctypes.util.find_library("libgfapi")
if api_gfapi_dll:
    api = ctypes.CDLL(api_gfapi_dll)

class GFApi:
    
    def __init__(self, **argv):
	self.fs = api.glfs_new(argv['volume'])
	self.directory = argv['directory']
	self.filename = argv['filename']
	self.dirfd = c_void_p
	api.glfs_set_logging(self.fs, "/dev/stderr", 7)
	api.glfs_set_volfile_server(self.fs, "tcp", "localhost", 24007)
	api.glfs_init(self.fs)

    def gf_opendir(self):
	self.dirfd = api.glfs_opendir(self.fs, self.directory)

    def gf_readdir(self):
	api.glfs_readdir_r(self.dirfd, self.entry, self.results)

    def gf_open(self):
	self.fd = api.glfs_open(self.fs, self.filename, os.O_RDWR)

    ## TODO
