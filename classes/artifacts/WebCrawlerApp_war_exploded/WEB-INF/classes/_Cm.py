# encoding: utf-8
# module _Cm
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_Cm.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def CloseComponentResFile(*args, **kwargs): # real signature unknown
    """ (short refnum) -> None """
    pass

def CountComponents(*args, **kwargs): # real signature unknown
    """ (ComponentDescription looking) -> (long _rv) """
    pass

def FindNextComponent(*args, **kwargs): # real signature unknown
    """ (Component aComponent, ComponentDescription looking) -> (Component _rv) """
    pass

def GetComponentListModSeed(*args, **kwargs): # real signature unknown
    """ () -> (long _rv) """
    pass

def OpenDefaultComponent(*args, **kwargs): # real signature unknown
    """ (OSType componentType, OSType componentSubType) -> (ComponentInstance _rv) """
    pass

def RegisterComponentResource(*args, **kwargs): # real signature unknown
    """ (ComponentResourceHandle cr, short global) -> (Component _rv) """
    pass

def RegisterComponentResourceFile(*args, **kwargs): # real signature unknown
    """ (short resRefNum, short global) -> (long _rv) """
    pass

# classes

class ComponentType(object):
    # no doc
    def CaptureComponent(self, *args, **kwargs): # real signature unknown
        """ (Component capturingComponent) -> (Component _rv) """
        pass

    def CountComponentInstances(self, *args, **kwargs): # real signature unknown
        """ () -> (long _rv) """
        pass

    def GetComponentIndString(self, *args, **kwargs): # real signature unknown
        """ (Str255 theString, short strListID, short index) -> None """
        pass

    def GetComponentInfo(self, *args, **kwargs): # real signature unknown
        """ (Handle componentName, Handle componentInfo, Handle componentIcon) -> (ComponentDescription cd) """
        pass

    def GetComponentPublicIndString(self, *args, **kwargs): # real signature unknown
        """ (Str255 theString, short strListID, short index) -> None """
        pass

    def GetComponentRefcon(self, *args, **kwargs): # real signature unknown
        """ () -> (long _rv) """
        pass

    def GetComponentResource(self, *args, **kwargs): # real signature unknown
        """ (OSType resType, short resID) -> (Handle theResource) """
        pass

    def OpenComponent(self, *args, **kwargs): # real signature unknown
        """ () -> (ComponentInstance _rv) """
        pass

    def OpenComponentResFile(self, *args, **kwargs): # real signature unknown
        """ () -> (short _rv) """
        pass

    def ResolveComponentAlias(self, *args, **kwargs): # real signature unknown
        """ () -> (Component _rv) """
        pass

    def SetComponentRefcon(self, *args, **kwargs): # real signature unknown
        """ (long theRefcon) -> None """
        pass

    def SetDefaultComponent(self, *args, **kwargs): # real signature unknown
        """ (short flags) -> None """
        pass

    def UncaptureComponent(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def UnregisterComponent(self, *args, **kwargs): # real signature unknown
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


Component = ComponentType


class ComponentInstanceType(object):
    # no doc
    def CloseComponent(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def GetComponentInstanceError(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def GetComponentInstanceStorage(self, *args, **kwargs): # real signature unknown
        """ () -> (Handle _rv) """
        pass

    def SetComponentInstanceError(self, *args, **kwargs): # real signature unknown
        """ (OSErr theError) -> None """
        pass

    def SetComponentInstanceStorage(self, *args, **kwargs): # real signature unknown
        """ (Handle theStorage) -> None """
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


ComponentInstance = ComponentInstanceType


