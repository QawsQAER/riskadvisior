# encoding: utf-8
# module _Res
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_Res.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def CloseResFile(*args, **kwargs): # real signature unknown
    """ (short refNum) -> None """
    pass

def Count1Resources(*args, **kwargs): # real signature unknown
    """ (ResType theType) -> (short _rv) """
    pass

def Count1Types(*args, **kwargs): # real signature unknown
    """ () -> (short _rv) """
    pass

def CountResources(*args, **kwargs): # real signature unknown
    """ (ResType theType) -> (short _rv) """
    pass

def CountTypes(*args, **kwargs): # real signature unknown
    """ () -> (short _rv) """
    pass

def CurResFile(*args, **kwargs): # real signature unknown
    """ () -> (short _rv) """
    pass

def DetachResourceFile(*args, **kwargs): # real signature unknown
    """ (SInt16 refNum) -> None """
    pass

def FSOpenResFile(*args, **kwargs): # real signature unknown
    """ (FSRef ref, SignedByte permission) -> (short _rv) """
    pass

def FSOpenResourceFile(*args, **kwargs): # real signature unknown
    """ (FSRef ref, Buffer forkNameLength, SignedByte permissions) -> (SInt16 refNum) """
    pass

def Get1IndResource(*args, **kwargs): # real signature unknown
    """ (ResType theType, short index) -> (Handle _rv) """
    pass

def Get1IndType(*args, **kwargs): # real signature unknown
    """ (short index) -> (ResType theType) """
    pass

def Get1NamedResource(*args, **kwargs): # real signature unknown
    """ (ResType theType, Str255 name) -> (Handle _rv) """
    pass

def Get1Resource(*args, **kwargs): # real signature unknown
    """ (ResType theType, short theID) -> (Handle _rv) """
    pass

def GetIndResource(*args, **kwargs): # real signature unknown
    """ (ResType theType, short index) -> (Handle _rv) """
    pass

def GetIndType(*args, **kwargs): # real signature unknown
    """ (short index) -> (ResType theType) """
    pass

def GetNamedResource(*args, **kwargs): # real signature unknown
    """ (ResType theType, Str255 name) -> (Handle _rv) """
    pass

def GetResFileAttrs(*args, **kwargs): # real signature unknown
    """ (short refNum) -> (short _rv) """
    pass

def GetResource(*args, **kwargs): # real signature unknown
    """ (ResType theType, short theID) -> (Handle _rv) """
    pass

def Handle(): # real signature unknown; restored from __doc__
    """
    Convert a string to a Handle object.
    
    Resource() and Handle() are very similar, but objects created with Handle() are
    by default automatically DisposeHandle()d upon object cleanup. Use AutoDispose()
    to change this.
    """
    pass

def InsertResourceFile(*args, **kwargs): # real signature unknown
    """ (SInt16 refNum, RsrcChainLocation where) -> None """
    pass

def ResError(*args, **kwargs): # real signature unknown
    """ () -> None """
    pass

def SetResFileAttrs(*args, **kwargs): # real signature unknown
    """ (short refNum, short attrs) -> None """
    pass

def SetResLoad(*args, **kwargs): # real signature unknown
    """ (Boolean load) -> None """
    pass

def SetResPurge(*args, **kwargs): # real signature unknown
    """ (Boolean install) -> None """
    pass

def Unique1ID(*args, **kwargs): # real signature unknown
    """ (ResType theType) -> (short _rv) """
    pass

def UniqueID(*args, **kwargs): # real signature unknown
    """ (ResType theType) -> (short _rv) """
    pass

def UpdateResFile(*args, **kwargs): # real signature unknown
    """ (short refNum) -> None """
    pass

def UseResFile(*args, **kwargs): # real signature unknown
    """ (short refNum) -> None """
    pass

# classes

class ResourceType(object):
    # no doc
    def AddResource(self, *args, **kwargs): # real signature unknown
        """ (ResType theType, short theID, Str255 name) -> None """
        pass

    def AutoDispose(self, *args, **kwargs): # real signature unknown
        """ (int)->int. Automatically DisposeHandle the object on Python object cleanup """
        pass

    def ChangedResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def DetachResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def GetMaxResourceSize(self, *args, **kwargs): # real signature unknown
        """ () -> (long _rv) """
        pass

    def GetNextFOND(self, *args, **kwargs): # real signature unknown
        """ () -> (Handle _rv) """
        pass

    def GetResAttrs(self, *args, **kwargs): # real signature unknown
        """ () -> (short _rv) """
        pass

    def GetResInfo(self, *args, **kwargs): # real signature unknown
        """ () -> (short theID, ResType theType, Str255 name) """
        pass

    def GetResourceSizeOnDisk(self, *args, **kwargs): # real signature unknown
        """ () -> (long _rv) """
        pass

    def HomeResFile(self, *args, **kwargs): # real signature unknown
        """ () -> (short _rv) """
        pass

    def LoadResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def MacLoadResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def ReleaseResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def RemoveResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def SetResAttrs(self, *args, **kwargs): # real signature unknown
        """ (short attrs) -> None """
        pass

    def SetResInfo(self, *args, **kwargs): # real signature unknown
        """ (short theID, Str255 name) -> None """
        pass

    def SetResourceSize(self, *args, **kwargs): # real signature unknown
        """ (long newSize) -> None """
        pass

    def WriteResource(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The resource data"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The length of the resource data"""



Resource = ResourceType


