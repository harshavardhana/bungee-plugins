import sys

import ctypes
import ctypes.util

from ctypes import c_char_p, c_int, c_size_t, c_void_p

class LibmagicException(Exception): pass

## ErrorCheck wrapper
def errorcheck(result, func, args):
    err = magic_error(args[0])
    if err is not None:
        raise LibmagicException(err)
    else:
        return result
## Encode Filename path with system Encoding
def encode_filename(filename):
    if filename is None:
        return None
    return filename.encode(sys.getfilesystemencoding())

libmagic = None
# Find magic or magic1
dll = ctypes.util.find_library('magic') or ctypes.util.find_library('magic1')

if dll:
    libmagic = ctypes.CDLL(dll)

if not libmagic or not libmagic._name:
    # Raise import error since libmagic not installed
    raise ImportError('failed to find libmagic.  Please install libmagic')

## Ctypes to PythonTypes conversion

magic_t = ctypes.c_void_p

magic_open = libmagic.magic_open
magic_open.restype = magic_t
magic_open.argtypes = [c_int]

magic_close = libmagic.magic_close
magic_close.restype = None
magic_close.argtypes = [magic_t]

magic_error = libmagic.magic_error
magic_error.restype = c_char_p
magic_error.argtypes = [magic_t]

magic_errno = libmagic.magic_errno
magic_errno.restype = c_int
magic_errno.argtypes = [magic_t]

_magic_buffer = libmagic.magic_buffer
_magic_buffer.restype = c_char_p
_magic_buffer.argtypes = [magic_t, c_void_p, c_size_t]
_magic_buffer.errcheck = errorcheck

_magic_load = libmagic.magic_load
_magic_load.restype = c_int
_magic_load.argtypes = [magic_t, c_char_p]
_magic_load.errcheck = errorcheck

magic_setflags = libmagic.magic_setflags
magic_setflags.restype = c_int
magic_setflags.argtypes = [magic_t, c_int]

magic_check = libmagic.magic_check
magic_check.restype = c_int
magic_check.argtypes = [magic_t, c_char_p]

magic_compile = libmagic.magic_compile
magic_compile.restype = c_int
magic_compile.argtypes = [magic_t, c_char_p]

## Read mime file buffer
def magic_buffer(cookie, buf):
    return _magic_buffer(cookie, buf, len(buf))

## Load magic mime database
def magic_load(cookie, filename):
    return _magic_load(cookie, coerce_filename(filename))
