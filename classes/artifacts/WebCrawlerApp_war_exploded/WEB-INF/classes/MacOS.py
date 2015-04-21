# encoding: utf-8
# module MacOS
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/MacOS.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

linkmodel = 'framework'

runtimemodel = 'macho'

string_id_to_buffer = 36

# functions

def GetCreatorAndType(*args, **kwargs): # real signature unknown
    """ Get MacOS 4-char creator and type for a file """
    pass

def GetErrorString(*args, **kwargs): # real signature unknown
    """ Convert OSErr number to string """
    pass

def GetTicks(*args, **kwargs): # real signature unknown
    """ Return number of ticks since bootup """
    pass

def openrf(*args, **kwargs): # real signature unknown
    """ Open resource fork of a file """
    pass

def SetCreatorAndType(*args, **kwargs): # real signature unknown
    """ Set MacOS 4-char creator and type for a file """
    pass

def WMAvailable(*args, **kwargs): # real signature unknown
    """ True if this process can interact with the display.Will foreground the application on the first call as a side-effect. """
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ResourceForkType(object):
    """ Resource fork file object """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


