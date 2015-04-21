# encoding: utf-8
# module _locale
# from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_locale.so
# by generator 1.136
""" Support for POSIX locales. """
# no imports

# Variables with simple values

ABDAY_1 = 14
ABDAY_2 = 15
ABDAY_3 = 16
ABDAY_4 = 17
ABDAY_5 = 18
ABDAY_6 = 19
ABDAY_7 = 20

ABMON_1 = 33
ABMON_10 = 42
ABMON_11 = 43
ABMON_12 = 44
ABMON_2 = 34
ABMON_3 = 35
ABMON_4 = 36
ABMON_5 = 37
ABMON_6 = 38
ABMON_7 = 39
ABMON_8 = 40
ABMON_9 = 41

ALT_DIGITS = 49

AM_STR = 5

CHAR_MAX = 127

CODESET = 0

CRNCYSTR = 56

DAY_1 = 7
DAY_2 = 8
DAY_3 = 9
DAY_4 = 10
DAY_5 = 11
DAY_6 = 12
DAY_7 = 13

D_FMT = 2

D_T_FMT = 1

ERA = 45

ERA_D_FMT = 46

ERA_D_T_FMT = 47

ERA_T_FMT = 48

LC_ALL = 0
LC_COLLATE = 1
LC_CTYPE = 2
LC_MESSAGES = 6
LC_MONETARY = 3
LC_NUMERIC = 4
LC_TIME = 5

MON_1 = 21
MON_10 = 30
MON_11 = 31
MON_12 = 32
MON_2 = 22
MON_3 = 23
MON_4 = 24
MON_5 = 25
MON_6 = 26
MON_7 = 27
MON_8 = 28
MON_9 = 29

NOEXPR = 53

PM_STR = 6

RADIXCHAR = 50

THOUSEP = 51

T_FMT = 3

T_FMT_AMPM = 4

YESEXPR = 52

# functions

def localeconv(*args, **kwargs): # real signature unknown
    """ () -> dict. Returns numeric and monetary locale-specific parameters. """
    pass

def nl_langinfo(key): # real signature unknown; restored from __doc__
    """
    nl_langinfo(key) -> string
    Return the value for the locale information associated with key.
    """
    return ""

def setlocale(*args, **kwargs): # real signature unknown
    """ (integer,string=None) -> string. Activates/queries locale processing. """
    pass

def strcoll(*args, **kwargs): # real signature unknown
    """ string,string -> int. Compares two strings according to the locale. """
    pass

def strxfrm(*args, **kwargs): # real signature unknown
    """ string -> string. Returns a string that behaves for cmp locale-aware. """
    pass

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



