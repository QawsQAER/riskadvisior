# encoding: utf-8
# module Quartz.CoreGraphics._callbacks
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC/Quartz/CoreGraphics/_callbacks.so
# by generator 1.136
# no doc
# no imports

# functions

def CGDataConsumerCreate(info, (putBytes, release)): # real signature unknown; restored from __doc__
    """
    CGDataConsumerCreate(info, (putBytes, release)) -> object
    
    putBytes and release are callback functions. Release may be None
    """
    return object()

def CGDataProviderCreateSequential(*args, **kwargs): # real signature unknown
    """
    CGDataConsumerCreateSequential(info, (getBytes, skipForward, rewind, releaseProvider)) -> object
    
    getBytes, skipForward, rewind and release are callback functions. Release may be None
    """
    pass

def CGDataProviderCreateWithData(info, data, size, release): # real signature unknown; restored from __doc__
    """ CGDataProviderCreateWithData(info, data, size, release) -> object """
    return object()

def CGDisplayRegisterReconfigurationCallback(*args, **kwargs): # real signature unknown
    pass

def CGDisplayRemoveReconfigurationCallback(*args, **kwargs): # real signature unknown
    pass

def CGEventTapCreate(*args, **kwargs): # real signature unknown
    pass

def CGEventTapCreateForPSN(*args, **kwargs): # real signature unknown
    pass

def CGFunctionCreate(info, domainDimension, domain, rangeDimension, range, evaluate): # real signature unknown; restored from __doc__
    """ CGFunctionCreate(info, domainDimension, domain, rangeDimension, range, evaluate) -> functionref """
    pass

def CGPatternCreate(*args, **kwargs): # real signature unknown
    pass

def CGPSConverterCreate(*args, **kwargs): # real signature unknown
    pass

def CGRegisterScreenRefreshCallback(*args, **kwargs): # real signature unknown
    pass

def CGScreenRegisterMoveCallback(*args, **kwargs): # real signature unknown
    pass

def CGScreenUnregisterMoveCallback(*args, **kwargs): # real signature unknown
    pass

def CGUnregisterScreenRefreshCallback(*args, **kwargs): # real signature unknown
    pass

# no classes
