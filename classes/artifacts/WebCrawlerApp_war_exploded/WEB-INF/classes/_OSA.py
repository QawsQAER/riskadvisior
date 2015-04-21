# encoding: utf-8
# module _OSA
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_OSA.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# no functions
# classes

class OSAComponentInstanceType(object):
    # no doc
    def OSAAvailableDialectCodeList(self, *args, **kwargs): # real signature unknown
        """ () -> (AEDesc resultingDialectCodeList) """
        pass

    def OSAAvailableDialects(self, *args, **kwargs): # real signature unknown
        """ () -> (AEDesc resultingDialectInfoList) """
        pass

    def OSACoerceFromDesc(self, *args, **kwargs): # real signature unknown
        """ (AEDesc scriptData, long modeFlags) -> (OSAID resultingScriptID) """
        pass

    def OSACoerceToDesc(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptID, DescType desiredType, long modeFlags) -> (AEDesc result) """
        pass

    def OSACompile(self, *args, **kwargs): # real signature unknown
        """ (AEDesc sourceData, long modeFlags) -> (OSAID previousAndResultingScriptID) """
        pass

    def OSACompileExecute(self, *args, **kwargs): # real signature unknown
        """ (AEDesc sourceData, OSAID contextID, long modeFlags) -> (OSAID resultingScriptValueID) """
        pass

    def OSACopyID(self, *args, **kwargs): # real signature unknown
        """ (OSAID fromID) -> (OSAID toID) """
        pass

    def OSADisplay(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptValueID, DescType desiredType, long modeFlags) -> (AEDesc resultingText) """
        pass

    def OSADispose(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptID) -> None """
        pass

    def OSADoEvent(self, *args, **kwargs): # real signature unknown
        """ (AppleEvent theAppleEvent, OSAID contextID, long modeFlags) -> (AppleEvent reply) """
        pass

    def OSADoScript(self, *args, **kwargs): # real signature unknown
        """ (AEDesc sourceData, OSAID contextID, DescType desiredType, long modeFlags) -> (AEDesc resultingText) """
        pass

    def OSAExecute(self, *args, **kwargs): # real signature unknown
        """ (OSAID compiledScriptID, OSAID contextID, long modeFlags) -> (OSAID resultingScriptValueID) """
        pass

    def OSAExecuteEvent(self, *args, **kwargs): # real signature unknown
        """ (AppleEvent theAppleEvent, OSAID contextID, long modeFlags) -> (OSAID resultingScriptValueID) """
        pass

    def OSAGetCurrentDialect(self, *args, **kwargs): # real signature unknown
        """ () -> (short resultingDialectCode) """
        pass

    def OSAGetDialectInfo(self, *args, **kwargs): # real signature unknown
        """ (short dialectCode, OSType selector) -> (AEDesc resultingDialectInfo) """
        pass

    def OSAGetScriptInfo(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptID, OSType selector) -> (long result) """
        pass

    def OSAGetSource(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptID, DescType desiredType) -> (AEDesc resultingSourceData) """
        pass

    def OSALoad(self, *args, **kwargs): # real signature unknown
        """ (AEDesc scriptData, long modeFlags) -> (OSAID resultingScriptID) """
        pass

    def OSALoadExecute(self, *args, **kwargs): # real signature unknown
        """ (AEDesc scriptData, OSAID contextID, long modeFlags) -> (OSAID resultingScriptValueID) """
        pass

    def OSAMakeContext(self, *args, **kwargs): # real signature unknown
        """ (AEDesc contextName, OSAID parentContext) -> (OSAID resultingContextID) """
        pass

    def OSAScriptError(self, *args, **kwargs): # real signature unknown
        """ (OSType selector, DescType desiredType) -> (AEDesc resultingErrorDescription) """
        pass

    def OSAScriptingComponentName(self, *args, **kwargs): # real signature unknown
        """ () -> (AEDesc resultingScriptingComponentName) """
        pass

    def OSASetCurrentDialect(self, *args, **kwargs): # real signature unknown
        """ (short dialectCode) -> None """
        pass

    def OSASetDefaultTarget(self, *args, **kwargs): # real signature unknown
        """ (AEAddressDesc target) -> None """
        pass

    def OSASetScriptInfo(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptID, OSType selector, long value) -> None """
        pass

    def OSAStartRecording(self, *args, **kwargs): # real signature unknown
        """ () -> (OSAID compiledScriptToModifyID) """
        pass

    def OSAStopRecording(self, *args, **kwargs): # real signature unknown
        """ (OSAID compiledScriptID) -> None """
        pass

    def OSAStore(self, *args, **kwargs): # real signature unknown
        """ (OSAID scriptID, DescType desiredType, long modeFlags) -> (AEDesc resultingScriptData) """
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


OSAComponentInstance = OSAComponentInstanceType


