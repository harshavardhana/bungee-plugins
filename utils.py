import sys
import os.path

from libmagic.constants import *
from libmagic import magic_load, magic_open, magic_close, magic_buffer

def mime_type(fd):
    """
    Identify the contents of `fd`
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
