
import errno
import os

class FS(object):

    """ Wrappers for necessary Filesystem calls done by bungee """
    def __init__ (self):
        self.__dir = None
        self.__old_fd = None

    @classmethod
    def dir(cls, directory):

        if not (type(directory) == type(str)):
            raise TypeError

        if len(directory) <= 0:
            raise AttributeError

        if len(directory) > 1024:
            raise errno.ENAMETOOLONG

        if os.path.exists(directory):
            self.__dir = directory

    @classmethod
    def findfile(cls):
        new_fd = None

        for i, j, k in os.walk(self.__dir):
            ##
            print i, j, k

        if not self.__old_fd is None:
            os.path.sameopenfile (self.__old_fd, new_fd)
