# encoding: utf-8
# module _CF
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_CF.so
# by generator 1.136
# no doc

# imports
from MacOS import Error


# functions

def CFAllocatorGetPreferredSizeForSize(*args, **kwargs): # real signature unknown
    """ (CFIndex size, CFOptionFlags hint) -> (CFIndex _rv) """
    pass

def CFAllocatorGetTypeID(*args, **kwargs): # real signature unknown
    """ () -> (CFTypeID _rv) """
    pass

def CFArrayCreateMutable(*args, **kwargs): # real signature unknown
    """ (CFIndex capacity) -> (CFMutableArrayRef _rv) """
    pass

def CFArrayCreateMutableCopy(*args, **kwargs): # real signature unknown
    """ (CFIndex capacity, CFArrayRef theArray) -> (CFMutableArrayRef _rv) """
    pass

def CFArrayGetTypeID(*args, **kwargs): # real signature unknown
    """ () -> (CFTypeID _rv) """
    pass

def CFCopyTypeIDDescription(*args, **kwargs): # real signature unknown
    """ (CFTypeID type_id) -> (CFStringRef _rv) """
    pass

def CFDataCreate(*args, **kwargs): # real signature unknown
    """ (Buffer bytes) -> (CFDataRef _rv) """
    pass

def CFDataCreateMutable(*args, **kwargs): # real signature unknown
    """ (CFIndex capacity) -> (CFMutableDataRef _rv) """
    pass

def CFDataCreateMutableCopy(*args, **kwargs): # real signature unknown
    """ (CFIndex capacity, CFDataRef theData) -> (CFMutableDataRef _rv) """
    pass

def CFDataCreateWithBytesNoCopy(*args, **kwargs): # real signature unknown
    """ (Buffer bytes) -> (CFDataRef _rv) """
    pass

def CFDataGetTypeID(*args, **kwargs): # real signature unknown
    """ () -> (CFTypeID _rv) """
    pass

def CFDictionaryCreateMutable(*args, **kwargs): # real signature unknown
    """ (CFIndex capacity) -> (CFMutableDictionaryRef _rv) """
    pass

def CFDictionaryCreateMutableCopy(*args, **kwargs): # real signature unknown
    """ (CFIndex capacity, CFDictionaryRef theDict) -> (CFMutableDictionaryRef _rv) """
    pass

def CFDictionaryGetTypeID(*args, **kwargs): # real signature unknown
    """ () -> (CFTypeID _rv) """
    pass

def CFPreferencesAddSuitePreferencesToApp(*args, **kwargs): # real signature unknown
    """ (CFStringRef applicationID, CFStringRef suiteID) -> None """
    pass

def CFPreferencesAppSynchronize(*args, **kwargs): # real signature unknown
    """ (CFStringRef applicationID) -> (Boolean _rv) """
    pass

def CFPreferencesCopyApplicationList(*args, **kwargs): # real signature unknown
    """ (CFStringRef userName, CFStringRef hostName) -> (CFArrayRef _rv) """
    pass

def CFPreferencesCopyAppValue(*args, **kwargs): # real signature unknown
    """ (CFStringRef key, CFStringRef applicationID) -> (CFTypeRef _rv) """
    pass

def CFPreferencesCopyKeyList(*args, **kwargs): # real signature unknown
    """ (CFStringRef applicationID, CFStringRef userName, CFStringRef hostName) -> (CFArrayRef _rv) """
    pass

def CFPreferencesCopyMultiple(*args, **kwargs): # real signature unknown
    """ (CFArrayRef keysToFetch, CFStringRef applicationID, CFStringRef userName, CFStringRef hostName) -> (CFDictionaryRef _rv) """
    pass

def CFPreferencesCopyValue(*args, **kwargs): # real signature unknown
    """ (CFStringRef key, CFStringRef applicationID, CFStringRef userName, CFStringRef hostName) -> (CFTypeRef _rv) """
    pass

def CFPreferencesGetAppBooleanValue(*args, **kwargs): # real signature unknown
    """ (CFStringRef key, CFStringRef applicationID) -> (Boolean _rv, Boolean keyExistsAndHasValidFormat) """
    pass

def CFPreferencesGetAppIntegerValue(*args, **kwargs): # real signature unknown
    """ (CFStringRef key, CFStringRef applicationID) -> (CFIndex _rv, Boolean keyExistsAndHasValidFormat) """
    pass

def CFPreferencesRemoveSuitePreferencesFromApp(*args, **kwargs): # real signature unknown
    """ (CFStringRef applicationID, CFStringRef suiteID) -> None """
    pass

def CFPreferencesSetAppValue(*args, **kwargs): # real signature unknown
    """ (CFStringRef key, CFTypeRef value, CFStringRef applicationID) -> None """
    pass

def CFPreferencesSetMultiple(*args, **kwargs): # real signature unknown
    """ (CFDictionaryRef keysToSet, CFArrayRef keysToRemove, CFStringRef applicationID, CFStringRef userName, CFStringRef hostName) -> None """
    pass

def CFPreferencesSetValue(*args, **kwargs): # real signature unknown
    """ (CFStringRef key, CFTypeRef value, CFStringRef applicationID, CFStringRef userName, CFStringRef hostName) -> None """
    pass

def CFPreferencesSynchronize(*args, **kwargs): # real signature unknown
    """ (CFStringRef applicationID, CFStringRef userName, CFStringRef hostName) -> (Boolean _rv) """
    pass

def CFStringConvertEncodingToIANACharSetName(*args, **kwargs): # real signature unknown
    """ (CFStringEncoding encoding) -> (CFStringRef _rv) """
    pass

def CFStringConvertEncodingToNSStringEncoding(*args, **kwargs): # real signature unknown
    """ (CFStringEncoding encoding) -> (UInt32 _rv) """
    pass

def CFStringConvertEncodingToWindowsCodepage(*args, **kwargs): # real signature unknown
    """ (CFStringEncoding encoding) -> (UInt32 _rv) """
    pass

def CFStringConvertNSStringEncodingToEncoding(*args, **kwargs): # real signature unknown
    """ (UInt32 encoding) -> (CFStringEncoding _rv) """
    pass

def CFStringConvertWindowsCodepageToEncoding(*args, **kwargs): # real signature unknown
    """ (UInt32 codepage) -> (CFStringEncoding _rv) """
    pass

def CFStringCreateMutable(*args, **kwargs): # real signature unknown
    """ (CFIndex maxLength) -> (CFMutableStringRef _rv) """
    pass

def CFStringCreateMutableCopy(*args, **kwargs): # real signature unknown
    """ (CFIndex maxLength, CFStringRef theString) -> (CFMutableStringRef _rv) """
    pass

def CFStringCreateWithBytes(*args, **kwargs): # real signature unknown
    """ (Buffer bytes, CFStringEncoding encoding, Boolean isExternalRepresentation) -> (CFStringRef _rv) """
    pass

def CFStringCreateWithCharacters(*args, **kwargs): # real signature unknown
    """ (Buffer chars) -> (CFStringRef _rv) """
    pass

def CFStringCreateWithCharactersNoCopy(*args, **kwargs): # real signature unknown
    """ (Buffer chars) -> (CFStringRef _rv) """
    pass

def CFStringCreateWithCString(*args, **kwargs): # real signature unknown
    """ (char* cStr, CFStringEncoding encoding) -> (CFStringRef _rv) """
    pass

def CFStringCreateWithCStringNoCopy(*args, **kwargs): # real signature unknown
    """ (char* cStr, CFStringEncoding encoding) -> (CFStringRef _rv) """
    pass

def CFStringCreateWithPascalString(*args, **kwargs): # real signature unknown
    """ (Str255 pStr, CFStringEncoding encoding) -> (CFStringRef _rv) """
    pass

def CFStringCreateWithPascalStringNoCopy(*args, **kwargs): # real signature unknown
    """ (Str255 pStr, CFStringEncoding encoding) -> (CFStringRef _rv) """
    pass

def CFStringGetMaximumSizeForEncoding(*args, **kwargs): # real signature unknown
    """ (CFIndex length, CFStringEncoding encoding) -> (CFIndex _rv) """
    pass

def CFStringGetMostCompatibleMacStringEncoding(*args, **kwargs): # real signature unknown
    """ (CFStringEncoding encoding) -> (CFStringEncoding _rv) """
    pass

def CFStringGetNameOfEncoding(*args, **kwargs): # real signature unknown
    """ (CFStringEncoding encoding) -> (CFStringRef _rv) """
    pass

def CFStringGetSystemEncoding(*args, **kwargs): # real signature unknown
    """ () -> (CFStringEncoding _rv) """
    pass

def CFStringGetTypeID(*args, **kwargs): # real signature unknown
    """ () -> (CFTypeID _rv) """
    pass

def CFStringIsEncodingAvailable(*args, **kwargs): # real signature unknown
    """ (CFStringEncoding encoding) -> (Boolean _rv) """
    pass

def CFURLCreateFromFileSystemRepresentation(*args, **kwargs): # real signature unknown
    """ (Buffer buffer, Boolean isDirectory) -> (CFURLRef _rv) """
    pass

def CFURLCreateFromFileSystemRepresentationRelativeToBase(*args, **kwargs): # real signature unknown
    """ (Buffer buffer, Boolean isDirectory, CFURLRef baseURL) -> (CFURLRef _rv) """
    pass

def CFURLCreateFromFSRef(*args, **kwargs): # real signature unknown
    """ (FSRef fsRef) -> (CFURLRef _rv) """
    pass

def CFURLCreateWithBytes(*args, **kwargs): # real signature unknown
    """ (Buffer URLBytes, CFStringEncoding encoding, CFURLRef baseURL) -> (CFURLRef _rv) """
    pass

def CFURLGetTypeID(*args, **kwargs): # real signature unknown
    """ () -> (CFTypeID _rv) """
    pass

def toCF(*args, **kwargs): # real signature unknown
    """ (python_object) -> (CF_object) """
    pass

def __CFRangeMake(*args, **kwargs): # real signature unknown
    """ (CFIndex loc, CFIndex len) -> (CFRange _rv) """
    pass

def __CFStringMakeConstantString(*args, **kwargs): # real signature unknown
    """ (char* cStr) -> (CFStringRef _rv) """
    pass

# classes

class CFTypeRefType(object):
    # no doc
    def CFCopyDescription(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFEqual(self, *args, **kwargs): # real signature unknown
        """ (CFTypeRef cf2) -> (Boolean _rv) """
        pass

    def CFGetRetainCount(self, *args, **kwargs): # real signature unknown
        """ () -> (CFIndex _rv) """
        pass

    def CFGetTypeID(self, *args, **kwargs): # real signature unknown
        """ () -> (CFTypeID _rv) """
        pass

    def CFHash(self, *args, **kwargs): # real signature unknown
        """ () -> (CFHashCode _rv) """
        pass

    def CFPropertyListCreateDeepCopy(self, *args, **kwargs): # real signature unknown
        """ (CFOptionFlags mutabilityOption) -> (CFTypeRef _rv) """
        pass

    def CFPropertyListCreateFromXMLData(self, *args, **kwargs): # real signature unknown
        """ (CFOptionFlags mutabilityOption) -> (CFTypeRefObj) """
        pass

    def CFPropertyListCreateXMLData(self, *args, **kwargs): # real signature unknown
        """ () -> (CFDataRef _rv) """
        pass

    def CFRelease(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CFRetain(self, *args, **kwargs): # real signature unknown
        """ () -> (CFTypeRef _rv) """
        pass

    def CFShow(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def toPython(self, *args, **kwargs): # real signature unknown
        """ () -> (python_object) """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFTypeRef = CFTypeRefType


class CFArrayRefType(CFTypeRef):
    # no doc
    def CFArrayCreateCopy(self, *args, **kwargs): # real signature unknown
        """ () -> (CFArrayRef _rv) """
        pass

    def CFArrayGetCount(self, *args, **kwargs): # real signature unknown
        """ () -> (CFIndex _rv) """
        pass

    def CFStringCreateByCombiningStrings(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef separatorString) -> (CFStringRef _rv) """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFArrayRef = CFArrayRefType


class CFDataRefType(CFTypeRef):
    # no doc
    def CFDataCreateCopy(self, *args, **kwargs): # real signature unknown
        """ () -> (CFDataRef _rv) """
        pass

    def CFDataGetData(self, *args, **kwargs): # real signature unknown
        """ () -> (string _rv) """
        pass

    def CFDataGetLength(self, *args, **kwargs): # real signature unknown
        """ () -> (CFIndex _rv) """
        pass

    def CFStringCreateFromExternalRepresentation(self, *args, **kwargs): # real signature unknown
        """ (CFStringEncoding encoding) -> (CFStringRef _rv) """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFDataRef = CFDataRefType


class CFDictionaryRefType(CFTypeRef):
    # no doc
    def CFDictionaryCreateCopy(self, *args, **kwargs): # real signature unknown
        """ () -> (CFDictionaryRef _rv) """
        pass

    def CFDictionaryGetCount(self, *args, **kwargs): # real signature unknown
        """ () -> (CFIndex _rv) """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFDictionaryRef = CFDictionaryRefType


class CFMutableArrayRefType(CFArrayRef):
    # no doc
    def CFArrayAppendArray(self, *args, **kwargs): # real signature unknown
        """ (CFArrayRef otherArray, CFRange otherRange) -> None """
        pass

    def CFArrayExchangeValuesAtIndices(self, *args, **kwargs): # real signature unknown
        """ (CFIndex idx1, CFIndex idx2) -> None """
        pass

    def CFArrayRemoveAllValues(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CFArrayRemoveValueAtIndex(self, *args, **kwargs): # real signature unknown
        """ (CFIndex idx) -> None """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFMutableArrayRef = CFMutableArrayRefType


class CFMutableDataRefType(CFDataRef):
    # no doc
    def CFDataAppendBytes(self, *args, **kwargs): # real signature unknown
        """ (Buffer bytes) -> None """
        pass

    def CFDataDeleteBytes(self, *args, **kwargs): # real signature unknown
        """ (CFRange range) -> None """
        pass

    def CFDataIncreaseLength(self, *args, **kwargs): # real signature unknown
        """ (CFIndex extraLength) -> None """
        pass

    def CFDataReplaceBytes(self, *args, **kwargs): # real signature unknown
        """ (CFRange range, Buffer newBytes) -> None """
        pass

    def CFDataSetLength(self, *args, **kwargs): # real signature unknown
        """ (CFIndex length) -> None """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFMutableDataRef = CFMutableDataRefType


class CFMutableDictionaryRefType(CFDictionaryRef):
    # no doc
    def CFDictionaryRemoveAllValues(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFMutableDictionaryRef = CFMutableDictionaryRefType


class CFStringRefType(CFTypeRef):
    # no doc
    def CFShowStr(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def CFStringCompare(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef theString2, CFOptionFlags compareOptions) -> (CFComparisonResult _rv) """
        pass

    def CFStringCompareWithOptions(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef theString2, CFRange rangeToCompare, CFOptionFlags compareOptions) -> (CFComparisonResult _rv) """
        pass

    def CFStringConvertIANACharSetNameToEncoding(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringEncoding _rv) """
        pass

    def CFStringCreateArrayBySeparatingStrings(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef separatorString) -> (CFArrayRef _rv) """
        pass

    def CFStringCreateArrayWithFindResults(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef stringToFind, CFRange rangeToSearch, CFOptionFlags compareOptions) -> (CFArrayRef _rv) """
        pass

    def CFStringCreateCopy(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFStringCreateExternalRepresentation(self, *args, **kwargs): # real signature unknown
        """ (CFStringEncoding encoding, UInt8 lossByte) -> (CFDataRef _rv) """
        pass

    def CFStringCreateWithSubstring(self, *args, **kwargs): # real signature unknown
        """ (CFRange range) -> (CFStringRef _rv) """
        pass

    def CFStringFind(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef stringToFind, CFOptionFlags compareOptions) -> (CFRange _rv) """
        pass

    def CFStringFindWithOptions(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef stringToFind, CFRange rangeToSearch, CFOptionFlags searchOptions) -> (Boolean _rv, CFRange result) """
        pass

    def CFStringGetBytes(self, *args, **kwargs): # real signature unknown
        """ (CFRange range, CFStringEncoding encoding, UInt8 lossByte, Boolean isExternalRepresentation, CFIndex maxBufLen) -> (CFIndex _rv, UInt8 buffer, CFIndex usedBufLen) """
        pass

    def CFStringGetDoubleValue(self, *args, **kwargs): # real signature unknown
        """ () -> (double _rv) """
        pass

    def CFStringGetFastestEncoding(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringEncoding _rv) """
        pass

    def CFStringGetIntValue(self, *args, **kwargs): # real signature unknown
        """ () -> (SInt32 _rv) """
        pass

    def CFStringGetLength(self, *args, **kwargs): # real signature unknown
        """ () -> (CFIndex _rv) """
        pass

    def CFStringGetLineBounds(self, *args, **kwargs): # real signature unknown
        """ (CFRange range) -> (CFIndex lineBeginIndex, CFIndex lineEndIndex, CFIndex contentsEndIndex) """
        pass

    def CFStringGetSmallestEncoding(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringEncoding _rv) """
        pass

    def CFStringGetString(self, *args, **kwargs): # real signature unknown
        """ () -> (string _rv) """
        pass

    def CFStringGetUnicode(self, *args, **kwargs): # real signature unknown
        """ () -> (unicode _rv) """
        pass

    def CFStringHasPrefix(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef prefix) -> (Boolean _rv) """
        pass

    def CFStringHasSuffix(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef suffix) -> (Boolean _rv) """
        pass

    def CFURLCreateStringByAddingPercentEscapes(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef charactersToLeaveUnescaped, CFStringRef legalURLCharactersToBeEscaped, CFStringEncoding encoding) -> (CFStringRef _rv) """
        pass

    def CFURLCreateStringByReplacingPercentEscapes(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef charactersToLeaveEscaped) -> (CFStringRef _rv) """
        pass

    def CFURLCreateWithFileSystemPath(self, *args, **kwargs): # real signature unknown
        """ (CFURLPathStyle pathStyle, Boolean isDirectory) -> (CFURLRef _rv) """
        pass

    def CFURLCreateWithFileSystemPathRelativeToBase(self, *args, **kwargs): # real signature unknown
        """ (CFURLPathStyle pathStyle, Boolean isDirectory, CFURLRef baseURL) -> (CFURLRef _rv) """
        pass

    def CFURLCreateWithString(self, *args, **kwargs): # real signature unknown
        """ (CFURLRef baseURL) -> (CFURLRef _rv) """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFStringRef = CFStringRefType


class CFMutableStringRefType(CFStringRef):
    # no doc
    def CFStringAppend(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef appendedString) -> None """
        pass

    def CFStringAppendCharacters(self, *args, **kwargs): # real signature unknown
        """ (Buffer chars) -> None """
        pass

    def CFStringAppendCString(self, *args, **kwargs): # real signature unknown
        """ (char* cStr, CFStringEncoding encoding) -> None """
        pass

    def CFStringAppendPascalString(self, *args, **kwargs): # real signature unknown
        """ (Str255 pStr, CFStringEncoding encoding) -> None """
        pass

    def CFStringDelete(self, *args, **kwargs): # real signature unknown
        """ (CFRange range) -> None """
        pass

    def CFStringInsert(self, *args, **kwargs): # real signature unknown
        """ (CFIndex idx, CFStringRef insertedStr) -> None """
        pass

    def CFStringPad(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef padString, CFIndex length, CFIndex indexIntoPad) -> None """
        pass

    def CFStringReplace(self, *args, **kwargs): # real signature unknown
        """ (CFRange range, CFStringRef replacement) -> None """
        pass

    def CFStringReplaceAll(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef replacement) -> None """
        pass

    def CFStringTrim(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef trimString) -> None """
        pass

    def CFStringTrimWhitespace(self, *args, **kwargs): # real signature unknown
        """ () -> None """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFMutableStringRef = CFMutableStringRefType


class CFURLRefType(CFTypeRef):
    # no doc
    def CFURLCanBeDecomposed(self, *args, **kwargs): # real signature unknown
        """ () -> (Boolean _rv) """
        pass

    def CFURLCopyAbsoluteURL(self, *args, **kwargs): # real signature unknown
        """ () -> (CFURLRef _rv) """
        pass

    def CFURLCopyFileSystemPath(self, *args, **kwargs): # real signature unknown
        """ (CFURLPathStyle pathStyle) -> (CFStringRef _rv) """
        pass

    def CFURLCopyFragment(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef charactersToLeaveEscaped) -> (CFStringRef _rv) """
        pass

    def CFURLCopyHostName(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyLastPathComponent(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyNetLocation(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyParameterString(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef charactersToLeaveEscaped) -> (CFStringRef _rv) """
        pass

    def CFURLCopyPassword(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyPath(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyPathExtension(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyQueryString(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef charactersToLeaveEscaped) -> (CFStringRef _rv) """
        pass

    def CFURLCopyResourceSpecifier(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyScheme(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCopyStrictPath(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv, Boolean isAbsolute) """
        pass

    def CFURLCopyUserName(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLCreateCopyAppendingPathComponent(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef pathComponent, Boolean isDirectory) -> (CFURLRef _rv) """
        pass

    def CFURLCreateCopyAppendingPathExtension(self, *args, **kwargs): # real signature unknown
        """ (CFStringRef extension) -> (CFURLRef _rv) """
        pass

    def CFURLCreateCopyDeletingLastPathComponent(self, *args, **kwargs): # real signature unknown
        """ () -> (CFURLRef _rv) """
        pass

    def CFURLCreateCopyDeletingPathExtension(self, *args, **kwargs): # real signature unknown
        """ () -> (CFURLRef _rv) """
        pass

    def CFURLCreateData(self, *args, **kwargs): # real signature unknown
        """ (CFStringEncoding encoding, Boolean escapeWhitespace) -> (CFDataRef _rv) """
        pass

    def CFURLGetBaseURL(self, *args, **kwargs): # real signature unknown
        """ () -> (CFURLRef _rv) """
        pass

    def CFURLGetFileSystemRepresentation(self, *args, **kwargs): # real signature unknown
        """ (Boolean resolveAgainstBase, CFIndex maxBufLen) -> (Boolean _rv, UInt8 buffer) """
        pass

    def CFURLGetFSRef(self, *args, **kwargs): # real signature unknown
        """ () -> (Boolean _rv, FSRef fsRef) """
        pass

    def CFURLGetPortNumber(self, *args, **kwargs): # real signature unknown
        """ () -> (SInt32 _rv) """
        pass

    def CFURLGetString(self, *args, **kwargs): # real signature unknown
        """ () -> (CFStringRef _rv) """
        pass

    def CFURLHasDirectoryPath(self, *args, **kwargs): # real signature unknown
        """ () -> (Boolean _rv) """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CFURLRef = CFURLRefType


# variables with complex values

kCFPreferencesAnyApplication = None # (!) real value is ''

kCFPreferencesAnyHost = None # (!) real value is ''

kCFPreferencesAnyUser = None # (!) real value is ''

kCFPreferencesCurrentApplication = None # (!) real value is ''

kCFPreferencesCurrentHost = None # (!) real value is ''

kCFPreferencesCurrentUser = None # (!) real value is ''

