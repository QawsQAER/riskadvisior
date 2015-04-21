# encoding: utf-8
# module autoGIL
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/autoGIL.so
# by generator 1.136
"""
The autoGIL module provides a function (installAutoGIL) that
automatically locks and unlocks Python's Global Interpreter Lock
when running an event loop.
"""
# no imports

# functions

def installAutoGIL(): # real signature unknown; restored from __doc__
    """
    installAutoGIL() -> None
    Install an observer callback in the event loop (CFRunLoop) for the
    current thread, that will lock and unlock the Global Interpreter Lock
    (GIL) at appropriate times, allowing other Python threads to run while
    the event loop is idle.
    """
    pass

# classes

class AutoGILError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



