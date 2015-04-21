# encoding: utf-8
# module _Launch
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_Launch.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def LSCanRefAcceptItem(*args, **kwargs): # real signature unknown
    """ (FSRef inItemFSRef, FSRef inTargetRef, LSRolesMask inRoleMask, LSAcceptanceFlags inFlags) -> (Boolean outAcceptsItem) """
    pass

def LSCanURLAcceptURL(*args, **kwargs): # real signature unknown
    """ (CFURLRef inItemURL, CFURLRef inTargetURL, LSRolesMask inRoleMask, LSAcceptanceFlags inFlags) -> (Boolean outAcceptsItem) """
    pass

def LSCopyDisplayNameForRef(*args, **kwargs): # real signature unknown
    """ (FSRef inRef) -> (CFStringRef outDisplayName) """
    pass

def LSCopyDisplayNameForURL(*args, **kwargs): # real signature unknown
    """ (CFURLRef inURL) -> (CFStringRef outDisplayName) """
    pass

def LSCopyItemInfoForRef(*args, **kwargs): # real signature unknown
    """ (FSRef inItemRef, LSRequestedInfo inWhichInfo) -> (LSItemInfoRecord outItemInfo) """
    pass

def LSCopyItemInfoForURL(*args, **kwargs): # real signature unknown
    """ (CFURLRef inURL, LSRequestedInfo inWhichInfo) -> (LSItemInfoRecord outItemInfo) """
    pass

def LSCopyKindStringForRef(*args, **kwargs): # real signature unknown
    """ (FSRef inFSRef) -> (CFStringRef outKindString) """
    pass

def LSCopyKindStringForURL(*args, **kwargs): # real signature unknown
    """ (CFURLRef inURL) -> (CFStringRef outKindString) """
    pass

def LSFindApplicationForInfo(*args, **kwargs): # real signature unknown
    """ (OSType inCreator, CFStringRef inBundleID, CFStringRef inName) -> (FSRef outAppRef, CFURLRef outAppURL) """
    pass

def LSGetApplicationForInfo(*args, **kwargs): # real signature unknown
    """ (OSType inType, OSType inCreator, CFStringRef inExtension, LSRolesMask inRoleMask) -> (FSRef outAppRef, CFURLRef outAppURL) """
    pass

def LSGetApplicationForItem(*args, **kwargs): # real signature unknown
    """ (FSRef inItemRef, LSRolesMask inRoleMask) -> (FSRef outAppRef, CFURLRef outAppURL) """
    pass

def LSGetApplicationForURL(*args, **kwargs): # real signature unknown
    """ (CFURLRef inURL, LSRolesMask inRoleMask) -> (FSRef outAppRef, CFURLRef outAppURL) """
    pass

def LSGetExtensionInfo(*args, **kwargs): # real signature unknown
    """ (Buffer inNameLen) -> (UniCharCount outExtStartIndex) """
    pass

def LSOpenCFURLRef(*args, **kwargs): # real signature unknown
    """ (CFURLRef inURL) -> (CFURLRef outLaunchedURL) """
    pass

def LSOpenFSRef(*args, **kwargs): # real signature unknown
    """ (FSRef inRef) -> (FSRef outLaunchedRef) """
    pass

def LSSetExtensionHiddenForRef(*args, **kwargs): # real signature unknown
    """ (FSRef inRef, Boolean inHide) -> None """
    pass

def LSSetExtensionHiddenForURL(*args, **kwargs): # real signature unknown
    """ (CFURLRef inURL, Boolean inHide) -> None """
    pass

# no classes
