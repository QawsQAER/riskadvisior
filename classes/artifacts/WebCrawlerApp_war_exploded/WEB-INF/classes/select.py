# encoding: utf-8
# module select
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/select.so
# by generator 1.136
"""
This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows and OpenVMS, only sockets are supported; on Unix, all file descriptors.
"""
# no imports

# Variables with simple values

KQ_EV_ADD = 1
KQ_EV_CLEAR = 32
KQ_EV_DELETE = 2
KQ_EV_DISABLE = 8
KQ_EV_ENABLE = 4
KQ_EV_EOF = 32768
KQ_EV_ERROR = 16384
KQ_EV_FLAG1 = 8192
KQ_EV_ONESHOT = 16
KQ_EV_SYSFLAGS = 61440

KQ_FILTER_AIO = -3
KQ_FILTER_PROC = -5
KQ_FILTER_READ = -1
KQ_FILTER_SIGNAL = -6
KQ_FILTER_TIMER = -7
KQ_FILTER_VNODE = -4
KQ_FILTER_WRITE = -2

KQ_NOTE_ATTRIB = 8
KQ_NOTE_CHILD = 4
KQ_NOTE_DELETE = 1
KQ_NOTE_EXEC = 536870912
KQ_NOTE_EXIT = -2147483648
KQ_NOTE_EXTEND = 4
KQ_NOTE_FORK = 1073741824
KQ_NOTE_LINK = 16
KQ_NOTE_LOWAT = 1
KQ_NOTE_PCTRLMASK = -1048576
KQ_NOTE_PDATAMASK = 1048575
KQ_NOTE_RENAME = 32
KQ_NOTE_REVOKE = 64
KQ_NOTE_TRACK = 1
KQ_NOTE_TRACKERR = 2
KQ_NOTE_WRITE = 2

PIPE_BUF = 512

# functions

def select(rlist, wlist, xlist, timeout=None): # real signature unknown; restored from __doc__
    """
    select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
    
    Wait until one or more file descriptors are ready for some kind of I/O.
    The first three arguments are sequences of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition''
    If only one kind of condition is required, pass [] for the other lists.
    A file descriptor is either a socket or file object, or a small integer
    gotten from a fileno() method call on one of those.
    
    The optional 4th argument specifies a timeout in seconds; it may be
    a floating point number to specify fractions of seconds.  If it is absent
    or None, the call will never time out.
    
    The return value is a tuple of three lists corresponding to the first three
    arguments; each contains the subset of the corresponding file descriptors
    that are ready.
    
    *** IMPORTANT NOTICE ***
    On Windows and OpenVMS, only sockets are supported; on Unix, all file
    descriptors can be used.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class kevent(object):
    """
    kevent(ident, filter=KQ_FILTER_READ, flags=KQ_EV_ADD, fflags=0, data=0, udata=0)
    
    This object is the equivalent of the struct kevent for the C API.
    
    See the kqueue manpage for more detailed information about the meaning
    of the arguments.
    
    One minor note: while you might hope that udata could store a
    reference to a python object, it cannot, because it is impossible to
    keep a proper reference count of the object once it's passed into the
    kernel. Therefore, I have restricted it to only storing an integer.  I
    recommend ignoring it and simply using the 'ident' field to key off
    of. You could also set up a dictionary on the python side to store a
    udata->object mapping.
    """
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, ident, filter=None, flags=None, fflags=0, data=0, udata=0): # real signature unknown; restored from __doc__
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ident = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    udata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class kqueue(object):
    """
    Kqueue syscall wrapper.
    
    For example, to start watching a socket for input:
    >>> kq = kqueue()
    >>> sock = socket()
    >>> sock.connect((host, port))
    >>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_ADD)], 0)
    
    To wait one second for it to become writeable:
    >>> kq.control(None, 1, 1000)
    
    To stop listening:
    >>> kq.control([kevent(sock, KQ_FILTER_WRITE, KQ_EV_DELETE)], 0)
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Close the kqueue control file descriptor. Further operations on the kqueue
        object will raise an exception.
        """
        pass

    def control(self, changelist, max_events, timeout=None): # real signature unknown; restored from __doc__
        """
        control(changelist, max_events[, timeout=None]) -> eventlist
        
        Calls the kernel kevent function.
        - changelist must be a list of kevent objects describing the changes
          to be made to the kernel's watch list or None.
        - max_events lets you specify the maximum number of events that the
          kernel will return.
        - timeout is the maximum time to wait in seconds, or else None,
          to wait forever. timeout accepts floats for smaller timeouts, too.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> int
        
        Return the kqueue control file descriptor.
        """
        return 0

    @classmethod
    def fromfd(cls, fd): # real signature unknown; restored from __doc__
        """
        fromfd(fd) -> kqueue
        
        Create a kqueue object from a given control fd.
        """
        return kqueue

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the kqueue handler is closed"""



