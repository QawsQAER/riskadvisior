# encoding: utf-8
# module _Folder
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_Folder.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def AddFolderDescriptor(*args, **kwargs): # real signature unknown
    """ (FolderType foldType, FolderDescFlags flags, FolderClass foldClass, FolderLocation foldLocation, OSType badgeSignature, OSType badgeType, Str255 name, Boolean replaceFlag) -> None """
    pass

def FindFolder(*args, **kwargs): # real signature unknown
    """ (short vRefNum, OSType folderType, Boolean createFolder) -> (short foundVRefNum, long foundDirID) """
    pass

def FSFindFolder(*args, **kwargs): # real signature unknown
    """ (short vRefNum, OSType folderType, Boolean createFolder) -> (FSRef foundRef) """
    pass

def GetFolderTypes(*args, **kwargs): # real signature unknown
    """ (UInt32 requestedTypeCount) -> (UInt32 totalTypeCount, FolderType theTypes) """
    pass

def IdentifyFolder(*args, **kwargs): # real signature unknown
    """ (short vRefNum, long dirID) -> (FolderType foldType) """
    pass

def InvalidateFolderDescriptorCache(*args, **kwargs): # real signature unknown
    """ (short vRefNum, long dirID) -> None """
    pass

def ReleaseFolder(*args, **kwargs): # real signature unknown
    """ (short vRefNum, OSType folderType) -> None """
    pass

def RemoveFolderDescriptor(*args, **kwargs): # real signature unknown
    """ (FolderType foldType) -> None """
    pass

# no classes
