import xattr

class XattrInfo:
    
    def __init__(self):
        self.ext_attributes = {}
    
    @classmethod
    def populate_ext_attr(cls, fd):
        """
        Function to populate extended attributes
        """
        if not isinstance(fd, int):
            raise ValueError('Invalid FD detected, integer value expected')

        xattrobj = xattr.xattr(fd)

        for name, value in xattrobj.iteritems():
            cls.ext_attributes['%s' % name] = '%s' % value
