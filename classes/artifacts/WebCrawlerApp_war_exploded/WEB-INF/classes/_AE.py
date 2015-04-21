# encoding: utf-8
# module _AE
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_AE.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def AECallObjectAccessor(*args, **kwargs): # real signature unknown
    """ (DescType desiredClass, AEDesc containerToken, DescType containerClass, DescType keyForm, AEDesc keyData) -> (AEDesc token) """
    pass

def AECoercePtr(*args, **kwargs): # real signature unknown
    """ (DescType typeCode, Buffer dataPtr, DescType toType) -> (AEDesc result) """
    pass

def AECreateAppleEvent(*args, **kwargs): # real signature unknown
    """ (AEEventClass theAEEventClass, AEEventID theAEEventID, AEAddressDesc target, AEReturnID returnID, AETransactionID transactionID) -> (AppleEvent result) """
    pass

def AECreateDesc(*args, **kwargs): # real signature unknown
    """ (DescType typeCode, Buffer dataPtr) -> (AEDesc result) """
    pass

def AECreateList(*args, **kwargs): # real signature unknown
    """ (Buffer factoringPtr, Boolean isRecord) -> (AEDescList resultList) """
    pass

def AEDisposeToken(*args, **kwargs): # real signature unknown
    """ () -> (AEDesc theToken) """
    pass

def AEGetEventHandler(*args, **kwargs): # real signature unknown
    """ (AEEventClass theAEEventClass, AEEventID theAEEventID) -> (EventHandler handler) """
    pass

def AEGetInteractionAllowed(*args, **kwargs): # real signature unknown
    """ () -> (AEInteractAllowed level) """
    pass

def AEInstallEventHandler(*args, **kwargs): # real signature unknown
    """ (AEEventClass theAEEventClass, AEEventID theAEEventID, EventHandler handler) -> None """
    pass

def AEInstallSpecialHandler(*args, **kwargs): # real signature unknown
    """ (AEKeyword functionClass) -> None """
    pass

def AEInteractWithUser(*args, **kwargs): # real signature unknown
    """ (long timeOutInTicks) -> None """
    pass

def AEManagerInfo(*args, **kwargs): # real signature unknown
    """ (AEKeyword keyWord) -> (long result) """
    pass

def AEObjectInit(*args, **kwargs): # real signature unknown
    """ () -> None """
    pass

def AEProcessAppleEvent(*args, **kwargs): # real signature unknown
    """ (EventRecord theEventRecord) -> None """
    pass

def AERemoveEventHandler(*args, **kwargs): # real signature unknown
    """ (AEEventClass theAEEventClass, AEEventID theAEEventID) -> None """
    pass

def AERemoveSpecialHandler(*args, **kwargs): # real signature unknown
    """ (AEKeyword functionClass) -> None """
    pass

def AEReplaceDescData(*args, **kwargs): # real signature unknown
    """ (DescType typeCode, Buffer dataPtr) -> (AEDesc theAEDesc) """
    pass

def AESetInteractionAllowed(*args, **kwargs): # real signature unknown
    """ (AEInteractAllowed level) -> None """
    pass

# classes

class AEDescType(object):
    # no doc
    def AECoerceDesc(self, *args, **kwargs): # real signature unknown
        """ (DescType toType) -> (AEDesc result) """
        pass

    def AECountItems(self, *args, **kwargs): # real signature unknown
        """ () -> (long theCount) """
        pass

    def AEDeleteItem(self, *args, **kwargs): # real signature unknown
        """ (long index) -> None """
        pass

    def AEDeleteParam(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword) -> None """
        pass

    def AEDuplicateDesc(self, *args, **kwargs): # real signature unknown
        """ () -> (AEDesc result) """
        pass

    def AEGetAttributeDesc(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, DescType desiredType) -> (AEDesc result) """
        pass

    def AEGetAttributePtr(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, DescType desiredType, Buffer dataPtr) -> (DescType typeCode, Buffer dataPtr) """
        pass

    def AEGetDescDataSize(self, *args, **kwargs): # real signature unknown
        """ () -> (Size _rv) """
        pass

    def AEGetNthDesc(self, *args, **kwargs): # real signature unknown
        """ (long index, DescType desiredType) -> (AEKeyword theAEKeyword, AEDesc result) """
        pass

    def AEGetNthPtr(self, *args, **kwargs): # real signature unknown
        """ (long index, DescType desiredType, Buffer dataPtr) -> (AEKeyword theAEKeyword, DescType typeCode, Buffer dataPtr) """
        pass

    def AEGetParamDesc(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, DescType desiredType) -> (AEDesc result) """
        pass

    def AEGetParamPtr(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, DescType desiredType, Buffer dataPtr) -> (DescType typeCode, Buffer dataPtr) """
        pass

    def AEGetTheCurrentEvent(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def AEPutAttributeDesc(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, AEDesc theAEDesc) -> None """
        pass

    def AEPutAttributePtr(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, DescType typeCode, Buffer dataPtr) -> None """
        pass

    def AEPutDesc(self, *args, **kwargs): # real signature unknown
        """ (long index, AEDesc theAEDesc) -> None """
        pass

    def AEPutParamDesc(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, AEDesc theAEDesc) -> None """
        pass

    def AEPutParamPtr(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword, DescType typeCode, Buffer dataPtr) -> None """
        pass

    def AEPutPtr(self, *args, **kwargs): # real signature unknown
        """ (long index, DescType typeCode, Buffer dataPtr) -> None """
        pass

    def AEResetTimer(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def AEResolve(self, *args, **kwargs): # real signature unknown
        """ (short callbackFlags) -> (AEDesc theToken) """
        pass

    def AEResumeTheCurrentEvent(self, *args, **kwargs): # real signature unknown
        """ (AppleEvent reply, EventHandler dispatcher) -> None """
        pass

    def AESend(self, *args, **kwargs): # real signature unknown
        """ (AESendMode sendMode, AESendPriority sendPriority, long timeOutInTicks) -> (AppleEvent reply) """
        pass

    def AESetTheCurrentEvent(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def AESizeOfAttribute(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword) -> (DescType typeCode, Size dataSize) """
        pass

    def AESizeOfNthItem(self, *args, **kwargs): # real signature unknown
        """ (long index) -> (DescType typeCode, Size dataSize) """
        pass

    def AESizeOfParam(self, *args, **kwargs): # real signature unknown
        """ (AEKeyword theAEKeyword) -> (DescType typeCode, Size dataSize) """
        pass

    def AESuspendTheCurrentEvent(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def AutoDispose(self, *args, **kwargs): # real signature unknown
        """ (int)->int. Automatically AEDisposeDesc the object on Python object cleanup """
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
    """The raw data in this AEDesc"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of this AEDesc"""



AEDesc = AEDescType


