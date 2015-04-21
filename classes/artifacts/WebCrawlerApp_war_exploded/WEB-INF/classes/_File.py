# encoding: utf-8
# module _File
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_File.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def FNNotifyAll(*args, **kwargs): # real signature unknown
    """ (FNMessage message, OptionBits flags) -> None """
    pass

def FNNotifyByPath(*args, **kwargs): # real signature unknown
    """ (UInt8 * path, FNMessage message, OptionBits flags) -> None """
    pass

def FSAllocateFork(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum, FSAllocationFlags flags, UInt16 positionMode, SInt64 positionOffset, UInt64 requestCount) -> (UInt64 actualCount) """
    pass

def FSCloseFork(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum) -> None """
    pass

def FSFlushFork(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum) -> None """
    pass

def FSGetDataForkName(*args, **kwargs): # real signature unknown
    """ () -> (HFSUniStr255 dataForkName) """
    pass

def FSGetForkPosition(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum) -> (SInt64 position) """
    pass

def FSGetForkSize(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum) -> (SInt64 forkSize) """
    pass

def FSGetResourceForkName(*args, **kwargs): # real signature unknown
    """ () -> (HFSUniStr255 resourceForkName) """
    pass

def FSNewAlias(*args, **kwargs): # real signature unknown
    """ (FSRef fromFile, FSRef target) -> (AliasHandle inAlias) """
    pass

def FSPathMakeRef(*args, **kwargs): # real signature unknown
    """ (UInt8 * path) -> (FSRef ref, Boolean isDirectory) """
    pass

def FSResolveAliasFile(*args, **kwargs): # real signature unknown
    """ (FSRef theRef, Boolean resolveAliasChains) -> (FSRef theRef, Boolean targetIsFolder, Boolean wasAliased) """
    pass

def FSResolveAliasFileWithMountFlags(*args, **kwargs): # real signature unknown
    """ (FSRef theRef, Boolean resolveAliasChains, unsigned long mountFlags) -> (FSRef theRef, Boolean targetIsFolder, Boolean wasAliased) """
    pass

def FSSetForkPosition(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum, UInt16 positionMode, SInt64 positionOffset) -> None """
    pass

def FSSetForkSize(*args, **kwargs): # real signature unknown
    """ (SInt16 forkRefNum, UInt16 positionMode, SInt64 positionOffset) -> None """
    pass

def FSUpdateAlias(*args, **kwargs): # real signature unknown
    """ (FSRef fromFile, FSRef target, AliasHandle alias) -> (Boolean wasChanged) """
    pass

def pathname(*args, **kwargs): # real signature unknown
    """ (str|unicode|FSSpec|FSref) -> pathname """
    pass

# classes

class AliasType(object):
    # no doc
    def FSFollowFinderAlias(self, *args, **kwargs): # real signature unknown
        """ (Boolean logon) -> (FSRef fromFile, FSRef target, Boolean wasChanged) """
        pass

    def FSResolveAlias(self, *args, **kwargs): # real signature unknown
        """ (FSRef fromFile) -> (FSRef target, Boolean wasChanged) """
        pass

    def FSResolveAliasWithMountFlags(self, *args, **kwargs): # real signature unknown
        """ (FSRef fromFile, unsigned long mountFlags) -> (FSRef target, Boolean wasChanged) """
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
    """Raw data of the alias object"""



Alias = AliasType


class FSCatalogInfoType(object):
    # no doc
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

    accessDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    attributeModDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backupDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contentModDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    createDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dataLogicalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dataPhysicalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nodeFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nodeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parentDirID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    permissions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rsrcLogicalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rsrcPhysicalSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sharingFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    userPrivileges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



FSCatalogInfo = FSCatalogInfoType


class FSRefType(object):
    # no doc
    def as_pathname(self, *args, **kwargs): # real signature unknown
        """ () -> string """
        pass

    def FNNotify(self, *args, **kwargs): # real signature unknown
        """ (FNMessage message, OptionBits flags) -> None """
        pass

    def FSCompareFSRefs(self, *args, **kwargs): # real signature unknown
        """ (FSRef ref2) -> None """
        pass

    def FSCreateDirectoryUnicode(self, *args, **kwargs): # real signature unknown
        """ (Buffer nameLength, FSCatalogInfoBitmap whichInfo, FSCatalogInfo catalogInfo) -> (FSRef newRef, FSSpec newSpec, UInt32 newDirID) """
        pass

    def FSCreateFileUnicode(self, *args, **kwargs): # real signature unknown
        """ (Buffer nameLength, FSCatalogInfoBitmap whichInfo, FSCatalogInfo catalogInfo) -> (FSRef newRef, FSSpec newSpec) """
        pass

    def FSCreateFork(self, *args, **kwargs): # real signature unknown
        """ (Buffer forkNameLength) -> None """
        pass

    def FSDeleteFork(self, *args, **kwargs): # real signature unknown
        """ (Buffer forkNameLength) -> None """
        pass

    def FSDeleteObject(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def FSExchangeObjects(self, *args, **kwargs): # real signature unknown
        """ (FSRef destRef) -> None """
        pass

    def FSGetCatalogInfo(self, *args, **kwargs): # real signature unknown
        """ (FSCatalogInfoBitmap whichInfo) -> (FSCatalogInfo catalogInfo, HFSUniStr255 outName, FSSpec fsSpec, FSRef parentRef) """
        pass

    def FSIsAliasFile(self, *args, **kwargs): # real signature unknown
        """ () -> (Boolean aliasFileFlag, Boolean folderFlag) """
        pass

    def FSMakeFSRefUnicode(self, *args, **kwargs): # real signature unknown
        """ (Buffer nameLength, TextEncoding textEncodingHint) -> (FSRef newRef) """
        pass

    def FSMoveObject(self, *args, **kwargs): # real signature unknown
        """ (FSRef destDirectory) -> (FSRef newRef) """
        pass

    def FSNewAliasMinimal(self, *args, **kwargs): # real signature unknown
        """ () -> (AliasHandle inAlias) """
        pass

    def FSOpenFork(self, *args, **kwargs): # real signature unknown
        """ (Buffer forkNameLength, SInt8 permissions) -> (SInt16 forkRefNum) """
        pass

    def FSRefMakePath(self, *args, **kwargs): # real signature unknown
        """ () -> string """
        pass

    def FSRenameUnicode(self, *args, **kwargs): # real signature unknown
        """ (Buffer nameLength, TextEncoding textEncodingHint) -> (FSRef newRef) """
        pass

    def FSSetCatalogInfo(self, *args, **kwargs): # real signature unknown
        """ (FSCatalogInfoBitmap whichInfo, FSCatalogInfo catalogInfo) -> None """
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
    """Raw data of the FSRef object"""



FSRef = FSRefType


