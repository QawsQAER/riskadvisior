# encoding: utf-8
# module objc._objc
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC/objc/_objc.so
# by generator 1.136
# no doc

# imports
import objc as __objc


# Variables with simple values

MAC_OS_X_VERSION_10_1 = 1010
MAC_OS_X_VERSION_10_2 = 1020
MAC_OS_X_VERSION_10_3 = 1030
MAC_OS_X_VERSION_10_4 = 1040
MAC_OS_X_VERSION_10_5 = 1050
MAC_OS_X_VERSION_10_6 = 1060
MAC_OS_X_VERSION_10_7 = 1070
MAC_OS_X_VERSION_10_8 = 1080

MAC_OS_X_VERSION_MAX_ALLOWED = 101000

MAC_OS_X_VERSION_MIN_REQUIRED = 101000

OBJC_ASSOCIATION_ASSIGN = 0
OBJC_ASSOCIATION_COPY = 771

OBJC_ASSOCIATION_COPY_NONATOMIC = 3

OBJC_ASSOCIATION_RETAIN = 769

OBJC_ASSOCIATION_RETAIN_NONATOMIC = 1

platform = 'MACOSX'

_C_ARY_B = '['
_C_ARY_E = ']'

_C_BFLD = 'b'
_C_BOOL = 'B'
_C_BYCOPY = 'O'
_C_CFIndex = 'q'
_C_CFTYPEID = 'Q'
_C_CGFloat = 'd'
_C_CHARPTR = '*'

_C_CHAR_AS_INT = 'z'
_C_CHAR_AS_TEXT = 't'

_C_CHR = 'c'
_C_CLASS = '#'
_C_CONST = 'r'
_C_DBL = 'd'
_C_FLT = 'f'
_C_ID = '@'
_C_IN = 'n'
_C_INOUT = 'N'
_C_INT = 'i'
_C_LNG = 'l'
_C_LNGLNG = 'q'

_C_LNG_LNG = 'q'

_C_NSBOOL = 'Z'
_C_NSInteger = 'q'
_C_NSUInteger = 'Q'
_C_ONEWAY = 'V'
_C_OUT = 'o'
_C_PTR = '^'
_C_SEL = ':'
_C_SHT = 's'

_C_STRUCT_B = '{'
_C_STRUCT_E = '}'

_C_UCHR = 'C'
_C_UINT = 'I'
_C_ULNG = 'L'
_C_ULNGLNG = 'Q'

_C_ULNG_LNG = 'Q'

_C_UNDEF = '?'
_C_UNICHAR = 'T'

_C_UNION_B = '('
_C_UNION_E = ')'

_C_USHT = 'S'
_C_VOID = 'v'

_size_sockaddr_ip4 = 16
_size_sockaddr_ip6 = 28

_sockaddr_type = '{sockaddr=CC[14c]}'

__version__ = '2.5.1'

# functions

def allocateBuffer(size): # real signature unknown; restored from __doc__
    """
    allocateBuffer(size) -> <r/w buffer>
    
    Allocate a buffer of memory of size. Buffer is 
    read/write.
    """
    pass

def CFToObject(cfObject): # real signature unknown; restored from __doc__
    """
    CFToObject(cfObject) -> objCObject
    
    Convert a CoreFoundation object to an Objective-C object. 
    Raises an exception if the conversion fails
    """
    pass

def classAddMethods(targetClass, methodsArray): # real signature unknown; restored from __doc__
    """
    classAddMethods(targetClass, methodsArray)
    
    Adds methods in methodsArray to class. The effect is similar to how 
    categories work. If class already implements a method as defined in 
    methodsArray, the original implementation will be replaced by the 
    implementation from methodsArray.
    """
    pass

def createOpaquePointerType(name, typestr, doc): # real signature unknown; restored from __doc__
    """
    createOpaquePointerType(name, typestr, doc) -> type
    
    Return a wrapper type for opaque pointers of the given type. The type 
    will be registered with PyObjC and will be used to wrap pointers of the 
    given type.
    """
    return type(*(), **{})

def createStructType(name, typestr, fieldnames, doc, pack): # real signature unknown; restored from __doc__
    """
    createStructType(name, typestr, fieldnames, doc, pack) -> type
    
    Return a wrapper type for structs of the given type. The wrapper will 
    registered with PyObjC and will be used to wrap structs of the given type.
    The field names can be ``None`` iff the typestr contains field names.
    """
    return type(*(), **{})

def currentBundle(): # real signature unknown; restored from __doc__
    """
    currentBundle() -> bundle
    
    Get the current bundle during module initialization.
    Works for plug-ins and applications.
    
    Note that this is the default bundle used by
    NibClassBuilder.extractClasses(...),
    so calling it explicitly is rarely useful.
    After module initialization, use
    NSBundle.bundleForClass_(ClassInYourBundle).
    """
    pass

def getAssociatedObject(p_object, key): # real signature unknown; restored from __doc__
    """
    getAssociatedObject(object, key) -> value
    
    Get the value for an object assiociation. Returns None 
    when they association doesn't exist.
    """
    pass

def getClassList(): # real signature unknown; restored from __doc__
    """
    getClassList() -> [ cls, ...] n
    Return a list with all Objective-C classes known to the runtime.
    """
    pass

def getInstanceVariable(p_object, name): # real signature unknown; restored from __doc__
    """
    getInstanceVariable(object, name) -> value
    
    Return the value of an instance variable
    """
    pass

def getObjCPointerIsError(): # real signature unknown; restored from __doc__
    """
    getObjCPointerIsError() -> bool
    
    Returns True if PyObjC raises an exception when it tries to wrap a pointer it doesn't know about.
    """
    return False

def getStrBridgeEnabled(): # real signature unknown; restored from __doc__
    """
    getStrBridgeEnabled() -> bool
    
    Return the status of the transparent str bridge.
    """
    return False

def getVerbose(): # real signature unknown; restored from __doc__
    """
    getVerbose() -> bool
    
    Return the verbosity value.
    """
    return False

def listInstanceVariables(classOrInstance): # real signature unknown; restored from __doc__
    """
    listInstanceVariables(classOrInstance) -> [ (name, typestr), ... ]
    
    Return information about all instance variables of an object or class
    """
    pass

def loadBundle(module_name, module_globals, bundle_path=None, bundle_identifier=None, scan_classes=True): # real signature unknown; restored from __doc__
    """
    loadBundle(module_name, module_globals, bundle_path=None, bundle_identifier=None, scan_classes=True) -> bundle
    
    Load the bundle identified by 'bundle_path' or 'bundle_identifier' 
    and add the classes in the bundle to the 'module_globals'.
    If 'scan_classes' is False the function won't add classes to 'module_globals'
    If 'bundle_identifier' is specified the right bundle is located
    using NSBundle's +bundleWithIdentifier:.
    If 'bundle_path' is specified the right bundle is located using
    NSBundle's +bundleWithPath:. The path must be an absolute pathname
    """
    pass

def loadBundleFunctions(bundle, module_globals, functionInfo, skip_undefined=True): # real signature unknown; restored from __doc__
    """
    loadBundleFunctions(bundle, module_globals, functionInfo, skip_undefined=True)
    
    Load the specified functions in the bundle. If skip_undefined is 
    True, variables that are not present in the bundle are skipped, 
    otherwise this method raises objc.error when a variable cannot be 
    found.
    
    functionInfo is a list of (name, signature, doc [, methinfo]) triples. 
    The signature is the Objective-C type specifier for the function 
    signature.
    """
    pass

def loadBundleVariables(bundle, module_globals, variableInfo, skip_undefined=True): # real signature unknown; restored from __doc__
    """
    loadBundleVariables(bundle, module_globals, variableInfo, skip_undefined=True)
    
    Load the specified variables in the bundle. If skip_undefined is 
    True, variables that are not present in the bundle are skipped, 
    otherwise this method raises objc.error when a variable cannot be 
    found.
    
    variableInfo is a list of (name, type) pairs. The type is the 
    Objective-C type specifier for the variable type.
    """
    pass

def loadFunctionList(p_list, module_globals, functionInfo, skip_undefined=True): # real signature unknown; restored from __doc__
    """
    loadFunctionList(list, module_globals, functionInfo, skip_undefined=True)
    
    Load the specified functions. List should be a capsule object containing
    an array of { char*, funcion } structs.
    """
    pass

def loadSpecialVar(*args, **kwargs): # real signature unknown
    pass

def lookUpClass(class_name): # real signature unknown; restored from __doc__
    """
    lookUpClass(class_name) -> class
    
    Search for the named classes in the Objective-C runtime and return it.
    Raises noclass_error when the class doesn't exist.
    """
    pass

def ObjectToCF(objCObject): # real signature unknown; restored from __doc__
    """
    ObjectToCF(objCObject) -> cfObject
    
    Convert an Objective-C object to a CoreFoundation object. 
    Raises an exception if the conversion fails
    """
    pass

def propertiesForClass(*args, **kwargs): # real signature unknown
    """ Return information about properties from the runtim """
    pass

def protocolsForClass(cls): # real signature unknown; restored from __doc__
    """
    protocolsForClass(cls) -> [Protocols]
    
    Returns a list of Protocol objects that the class claims
    to implement directly.
    """
    pass

def protocolsForProcess(): # real signature unknown; restored from __doc__
    """
    protocolsForProcess() -> [Protocols]
    
    Returns a list of Protocol objects that are present in the process
    """
    pass

def pyobjc_id(obj): # real signature unknown; restored from __doc__
    """
    pyobjc_id(obj) -> int
    
    Return the id of the underlying NSObject as an int.
    """
    return 0

def recycleAutoreleasePool(): # real signature unknown; restored from __doc__
    """
    recycleAutoreleasePool()
    
    This 'releases' the global autorelease pool and creates a new one.
    This method is for system use only
    """
    pass

def registerCFSignature(name, encoding, typeId, tollfreeName=None): # real signature unknown; restored from __doc__
    """
    registerCFSignature(name, encoding, typeId [, tollfreeName]) -> type
    
    Register a CoreFoundation based type with the bridge. If 
    tollFreeName is supplied the type is tollfree bridged to that class.
    """
    return type(*(), **{})

def registerMetaDataForSelector(p_class, selector, metadata): # real signature unknown; restored from __doc__
    """
    registerMetaDataForSelector(class, selector, metadata) -> None
    
    XXX: work out documentation.
    """
    pass

def registerStructAlias(typestr, structType): # real signature unknown; restored from __doc__
    """
    registerStructAlias(typestr, structType)
    
    Registers 'typestr' as a type that should be mapped onto 'structType'
    'structType' must be created using 'createStructType' (or through 
    a metadata file.
    """
    pass

def removeAssociatedObjects(p_object): # real signature unknown; restored from __doc__
    """
    removeAssociatedObjects(object)
    
    Remove all assocations from an object. This should in general not be used because
    it clear all references, including those made from unrelated code.
    """
    pass

def removeAutoreleasePool(): # real signature unknown; restored from __doc__
    """
    removeAutoreleasePool()
    
    This removes the global NSAutoreleasePool.  You should do this
    at the end of a plugin's initialization script.
    """
    pass

def repythonify(obj, type=None): # real signature unknown; restored from __doc__
    """
    repythonify(obj, type='@') -> object
    
    Put an object through the bridge by calling 
    depythonify_c_value then pythonify_c_value.
    This is for internal use only.
    """
    return object()

def setAssociatedObject(p_object, key, value, policy=None): # real signature unknown; restored from __doc__
    """
    setAssociatedObject(object, key, value, [policy=objc.OBJC_ASSOCIATION_RETAIN])
    
    Set the value for an object assiociation. Use 'None' as the
    value to clear an association.
    """
    pass

def setHideProtected(bool): # real signature unknown; restored from __doc__
    """
    setHideProtected(bool) -> None
    
    If true methods whose name starts with an underscore will not visible for introspection using dir() or the class __dict__.
    """
    pass

def setInstanceVariable(p_object, name, value, updateRefCount=None): # real signature unknown; restored from __doc__
    """
    setInstanceVariable(object, name, value [, updateRefCount])
    
    Modify an instance variable. If the instance variable is an object 
    reference you must include the ``updateRefCount`` argument, otherwise it 
    is ignored. If ``updateRefCount`` is true the reference counts of the 
    old and new values are updated, otherwise they are not.
    
    NOTE: updating instance variables is dangerous, instance variables are 
    private in Objective-C and classes might not expected that those values 
    are changed by other code.
    """
    pass

def setObjCPointerIsError(bool): # real signature unknown; restored from __doc__
    """
    setObjCPointerIsError(bool) -> None
    
    If the argument is True PyObjC will raise an exception when it tries to wrap a C pointer it doesn't know about.
    """
    pass

def setSignatureForSelector(class_name, selector, signature): # real signature unknown; restored from __doc__
    """
    setSignatureForSelector(class_name, selector, signature) -> None
    
    Register a replacement signature for a specific selector. This 
    can be used to provide a more exact signature for a method.
    
    This function is deprecated, use the new metadata machinery.
    """
    pass

def setStrBridgeEnabled(bool): # real signature unknown; restored from __doc__
    """
    setStrBridgeEnabled(bool)
    
    False disables the transparent str bridge (not default) 
    True enables the transparent str bridge
    """
    pass

def setUseKVOForSetattr(bool): # real signature unknown; restored from __doc__
    """
    setUseKVOForSetattr(bool) -> bool
    
    Specify the default value for __useKVO__ on classes defined after this call. Returns the previous value.
    """
    return False

def setVerbose(bool): # real signature unknown; restored from __doc__
    """
    setVerbose(bool) -> None
    
    Set verbosity to the new value.
    """
    pass

def splitSignature(signature): # real signature unknown; restored from __doc__
    """
    splitSignature(signature) -> list
    
    Split a signature string into a list of items.
    """
    return []

def splitStructSignature(signature): # real signature unknown; restored from __doc__
    """
    splitStructSignature(signature) -> structname, fields
    
    Split a struct signature string into a list of items.
    """
    pass

def _block_call(block, signature, args, kwds): # real signature unknown; restored from __doc__
    """ _block_call(block, signature, args, kwds) -> retval """
    pass

def _clear_intern(*args, **kwargs): # real signature unknown
    pass

def _getNSNumberWrapper(): # real signature unknown; restored from __doc__
    """
    _getNSNumberWrapper() -> wrapper
    
    Get the current NSNumber wrapper function.
    """
    pass

def _ivar_dict(*args, **kwargs): # real signature unknown
    """ private functions """
    pass

def _loadConstant(*args, **kwargs): # real signature unknown
    """ (PRIVATE) """
    pass

def _makeClosure(callable, closureFor, argIndex=None): # real signature unknown; restored from __doc__
    """
    _makeClosure(callable, closureFor, [argIndex]) -> closure
    
    Returns a closure object that can be used to call the function from
    C. This object has no useable interface from Python.
    """
    pass

def _objc_sync_enter(*args, **kwargs): # real signature unknown
    """ acquire mutex for an object """
    pass

def _objc_sync_exit(*args, **kwargs): # real signature unknown
    """ release mutex for an object """
    pass

def _protocolNamed(name): # real signature unknown; restored from __doc__
    """ _protocolNamed(name) -> Protocol """
    pass

def _setClassExtender(*args, **kwargs): # real signature unknown
    """
    setClassExtender(func) -> None
    
    Register a function that will be called to update the class
    dict of new Objective-C classes and class-proxies. This will
    replace any existing callback.
    The function will be called like this:
    	class_extender(superclass, class_name, class_dict)
    superclass:
      The superclass for the new class, or None if this is the top of
      a class hierarchy.
    class_name:
      Name of the new class
    class_dict:
      The proposed class dictionary. The callback is supposed to update
      this dictionary.
    """
    pass

def _setClassSetUpHook(*args, **kwargs): # real signature unknown
    """ Private: set hook used during subclass creation """
    pass

def _setNSNumberWrapper(wrapper): # real signature unknown; restored from __doc__
    """
    _setNSNumberWrapper(wrapper) -> None
    
    Set the NSNumber wrapper function to the new value.
    """
    pass

def _sockaddrFromPython(*args, **kwargs): # real signature unknown
    """ private function """
    pass

def _sockaddrToPython(*args, **kwargs): # real signature unknown
    """ private function """
    pass

def _typestr2typestr(*args, **kwargs): # real signature unknown
    """ private function """
    pass

def _updatingMetadata(*args, **kwargs): # real signature unknown
    """ PRIVATE: """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class BadPrototypeError(__objc.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class formal_protocol(object):
    """
    objc.formal_protocol(name, supers, selector_list)
    
    This class is used to proxy Objective-C formal protocols, and can also be 
    used to define new formal protocols.
    """
    def classMethods(self, *args, **kwargs): # real signature unknown
        """ List of class methods in this protocol """
        pass

    def conformsTo_(self, *args, **kwargs): # real signature unknown
        """ Does this protocol conform to another protocol """
        pass

    def descriptionForClassMethod_(self, *args, **kwargs): # real signature unknown
        """ Description for a class method in the protocol """
        pass

    def descriptionForInstanceMethod_(self, *args, **kwargs): # real signature unknown
        """ Description for an instance method in the protocol """
        pass

    def instanceMethods(self, *args, **kwargs): # real signature unknown
        """ List of instance methods in this protocol """
        pass

    def name(self, *args, **kwargs): # real signature unknown
        """ Return the  protocol name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, name, supers, selector_list): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __class__ = type
    __name__ = 'formal_protocol'


class FSRef(object):
    # no doc
    def as_carbon(self, *args, **kwargs): # real signature unknown
        """ return Carbon.File.FSRef instance for this object """
        pass

    def as_pathname(self, *args, **kwargs): # real signature unknown
        """ return POSIX path for this object (Unicode string) """
        pass

    @classmethod
    def from_pathname(cls, *args, **kwargs): # real signature unknown
        """ create FSRef instance for an POSIX path """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """bytes in the FSRef"""



class FSSpec(object):
    # no doc
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """bytes in the FSSpec"""



class function(object):
    """ Wrapper around a Objective-C function """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __metadata__(self, *args, **kwargs): # real signature unknown
        """ Return a dict that describes the metadata for this function. """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __name__ = 'function'


class IMP(object):
    # no doc
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __metadata__(self, *args, **kwargs): # real signature unknown
        """ Return metadata for the method """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    isAlloc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this is method returns a a freshly allocated object (uninitialized)

NOTE: This field is used by the implementation."""

    isClassMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this is a class method, False otherwise"""

    selector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Objective-C name for the IMP"""

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Objective-C signature for the IMP"""


    __name__ = 'IMP'


class informal_protocol(object):
    """
    objc.informal_protocol(name, selector_list)
    
    This class can be used to specify which methods are supported by an informal
    protocol. Instances of this type can by used while creating subclasses of 
    objective-C classes to automaticly specify method signatures et.al.
    """
    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, name, selector_list): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    selectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'informal_protocol'


class internal_error(__objc.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ivar(object):
    """
    ivar(name, type='@', isOutlet=False) -> instance-variable
    
    Creates a descriptor for accessing an Objective-C instance variable.
    
    This should only be used in the definition of Objective-C subclasses, and
    will then automaticly define the instance variable in the objective-C side.
    
    'type' is optional and should be a signature string.
    
    The name is optional in class definitions and will default to the name the
    value is assigned to
    """
    @classmethod
    def bool(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def BOOL(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def char(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def char_int(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def char_text(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def double(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def float(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def int(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def long(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def long_long(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def short(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def UniChar(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def unsigned_char(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def unsigned_int(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def unsigned_long(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def unsigned_long_long(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def unsigned_short(cls, *args, **kwargs): # real signature unknown
        pass

    def __delete__(self, obj): # real signature unknown; restored from __doc__
        """ descr.__delete__(obj) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, name, type=None, isOutlet=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __pyobjc_class_setup__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __set__(self, obj, value): # real signature unknown; restored from __doc__
        """ descr.__set__(obj, value) """
        pass

    __isOutlet__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the instance variable is an IBOutlet"""

    __isSlot__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the instance variable is a Python slot"""

    __typestr__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Objective-C type encoding"""


    __name__ = 'ivar'


class LockError(__objc.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class nosuchclass_error(__objc.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class objc_class(type):
    """
    objc_class(name, bases, dict) -> a new Objective-C class
    
    objc_class is the meta-type for Objective-C classes. It should not be
    necessary to manually create instances of this type, those are 
    created by subclassing and existing Objective-C class.
    
    The list of bases must start with an existing Objective-C class, and 
    cannot contain other Objective-C classes. The list may contain
    informal_interface objects, those are used during the calculation of
    method signatures and will not be visible in the list of base-classes
    of the created class.
    """
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, name, bases, dict): # real signature unknown; restored from __doc__
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    pyobjc_classMethods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The attributes of this field are the class methods of this object. This can
be used to force access to a class method."""

    pyobjc_instanceMethods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The attributes of this field are the instance methods of this object. This 
can be used to force access to an instance method."""

    __useKVO__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use KVO notifications when setting attributes from Python"""

    __version__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """get/set the version of a class"""


    __name__ = 'objc_class'


class objc_object(object):
    # no doc
    def __cobject__(self, *args, **kwargs): # real signature unknown
        """ Return a CObject representing this object """
        pass

    def __c_void_p__(self, *args, **kwargs): # real signature unknown
        """ Return a ctypes.c_void_p representing this object """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Used for pickling """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    pyobjc_ISA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the current ISA of the object"""

    __block_signature__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Call signature for a block, or None"""


    pyobjc_instanceMethods = None # (!) real value is ''


class PyObjCStrBridgeWarning(DeprecationWarning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class pyobjc_unicode(unicode):
    """
    objc.pyobjc_unicode
    
    Subclass of unicode for representing NSString values. Use 
    the method nsstring to access the NSString. 
    Note that instances are immutable and won't be updated when
    the value of the NSString changes.
    """
    def nsstring(self, *args, **kwargs): # real signature unknown
        """ directly access NSString instance """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Used for pickling """
        pass

    __pyobjc_object__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """raw NSString instance"""



class RevivedObjectiveCObjectWarning(Warning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class selector(object):
    """
    selector(function, [, selector] [, signature] [, isClassMethod=0]
        [, returnType] [, argumentTypes] [, isRequired=True]) -> selector
    
    Return an Objective-C method from a function. The other arguments 
    specify attributes of the Objective-C method.
    
    function:
      A function object with at least one argument. The first argument will
      be used to pass 'self'. This argument may be None when defining an
      informal_protocol object. The function must not be a ``staticmethod``
      instance. 
    selector:
      The name of the Objective-C method. The default value of this
      attribute is the name of the function, with all underscores replaced
      by colons.
    signature:
      Method signature for the Objective-C method. This should be a raw
      Objective-C method signature, including specifications for 'self' and
      '_cmd'. The default value a signature that describes a method with
      arguments of type 'id' and a return-value of the same type.
    argumentTypes, returnType:
      Alternative method for specifying the method signature. returnType is
      the return type and argumentTypes describes the list of arguments. The 
      returnType is optional and defaults to 'void' (e.g. no return value).
      Both are specified using a subset of the Py_BuildValue syntax:
      - s, z, S: an NSString (id)
      - b: a byte (char)
      - h: a short integer (short int)
      - i: an integer (int)
      - l: a long integer (long int)
      - c: a single character (char)
      - f: a single precision float (float)
      - d: a double precision float (double)
      - O: any object (id)
      It is not allowed to specify both 'argumentTypes' and 'signature'
    isClassMethod:
      True if the method is a class method, false otherwise. The default is 
      False, unless the function is an instance of ``classmethod``.
    isRequired:
      True if this is a required method in an informal protocol, False
      otherwise. The default value is 'True'. This argument is only used
      when defining an 'informal_protocol' object.
    """
    def __delete__(self, obj): # real signature unknown; restored from __doc__
        """ descr.__delete__(obj) """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, function, selector=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __metadata__(self, *args, **kwargs): # real signature unknown
        """ Return a dict that describes the metadata for this method, including metadata for the 2 hidden ObjC parameters (self and _sel) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __set__(self, obj, value): # real signature unknown; restored from __doc__
        """ descr.__set__(obj, value) """
        pass

    definingClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Objective-C Class that defines the method"""

    isClassMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this is a class method, False otherwise"""

    isHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True the method is not directly accessible as an object attribute"""

    isRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if this is a required method, False otherwise"""

    native_signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """original Objective-C signature for the method"""

    selector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Objective-C name for the method"""

    self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """'self' object for bound methods, None otherwise"""

    signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Objective-C signature for the method"""


    __name__ = 'selector'


class super(object):
    """
    super(type, obj) -> bound super object; requires isinstance(obj, type)
    super(type) -> unbound super object
    super(type, type2) -> bound super object; requires issubclass(type2, type)
    Typical use to call a cooperative superclass method:
    class C(B):
        def meth(self, arg):
            super(C, self).meth(arg)
    """
    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, type, obj): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class UninitializedDeallocWarning(Warning):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class UnknownPointerError(__objc.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class varlist(object):
    """
    objc.varlist
    
    A list of an unspecified size. Use ``obj.as_tuple(count)`` to 
    convertto a python tuple, or ``obj[index]`` to fetch a single item
    """
    def as_tuple(self, count): # real signature unknown; restored from __doc__
        """
        as_tuple(count)
        
        Return a tuple containing the first ``count`` elements of this list
        """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __delslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__delslice__(i, j) <==> del x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __setslice__(self, i, j, y): # real signature unknown; restored from __doc__
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
                   
                   Use  of negative indices is not supported.
        """
        pass


# variables with complex values

NULL = None # (!) real value is ''

__C_API__ = None # (!) real value is ''

