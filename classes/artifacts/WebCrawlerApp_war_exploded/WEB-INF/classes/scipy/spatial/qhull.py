# encoding: utf-8
# module scipy.spatial.qhull
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/spatial/qhull.so
# by generator 1.136
"""
Wrappers for Qhull triangulation, plus some additional N-D geometry utilities

.. versionadded:: 0.9
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import threading as threading # /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.pyc
import numpy as np # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.pyc

# functions

def tsearch(tri, xi): # real signature unknown; restored from __doc__
    """
    tsearch(tri, xi)
    
        Find simplices containing the given points. This function does the
        same thing as `Delaunay.find_simplex`.
    
        .. versionadded:: 0.9
    
        See Also
        --------
        Delaunay.find_simplex
    """
    pass

def _get_barycentric_transforms(*args, **kwargs): # real signature unknown
    """
    Compute barycentric affine coordinate transformations for given
        simplices.
    
        Returns
        -------
        Tinvs : array, shape (nsimplex, ndim+1, ndim)
            Barycentric transforms for each simplex.
    
            Tinvs[i,:ndim,:ndim] contains inverse of the matrix ``T``,
            and Tinvs[i,ndim,:] contains the vector ``r_n`` (see below).
    
        Notes
        -----
        Barycentric transform from ``x`` to ``c`` is defined by::
    
            T c = x - r_n
    
        where the ``r_1, ..., r_n`` are the vertices of the simplex.
        The matrix ``T`` is defined by the condition::
    
            T e_j = r_j - r_n
    
        where ``e_j`` is the unit axis vector, e.g, ``e_2 = [0,1,0,0,...]``
        This implies that ``T_ij = (r_j - r_n)_i``.
    
        For the barycentric transforms, we need to compute the inverse
        matrix ``T^-1`` and store the vectors ``r_n`` for each vertex.
        These are stacked into the `Tinvs` returned.
    """
    pass

# classes

class asbytes(basestring):
    """
    str(object='') -> string
    
    Return a nice string representation of the object.
    If the argument is a string, the return value is the same object.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> string
        
        Return a copy of the string S with only its first character
        capitalized.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> string
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are interpreted
        as in slice notation.
        """
        return 0

    def decode(self, encoding=None, errors=None): # real signature unknown; restored from __doc__
        """
        S.decode([encoding[,errors]]) -> object
        
        Decodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
        as well as any other name registered with codecs.register_error that is
        able to handle UnicodeDecodeErrors.
        """
        return object()

    def encode(self, encoding=None, errors=None): # real signature unknown; restored from __doc__
        """
        S.encode([encoding[,errors]]) -> object
        
        Encodes S using the codec registered for encoding. encoding defaults
        to the default encoding. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that is able to handle UnicodeEncodeErrors.
        """
        return object()

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=None): # real signature unknown; restored from __doc__
        """
        S.expandtabs([tabsize]) -> string
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub [,start [,end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> string
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub [,start [,end]]) -> int
        
        Like S.find() but raise ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. uppercase characters may only follow uncased
        characters and lowercase characters only cased ones. Return False
        otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> string
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> string
        
        Return S left-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> string
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> string or unicode
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> string
        
        Return a copy of string S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub [,start [,end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub [,start [,end]]) -> int
        
        Like S.rfind() but raise ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> string
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
        """
        S.rsplit([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string, starting at the end of the string and working
        to the front.  If maxsplit is given, at most maxsplit splits are
        done. If sep is not specified or is None, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> string or unicode
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def split(self, sep=None, maxsplit=None): # real signature unknown; restored from __doc__
        """
        S.split([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are removed
        from the result.
        """
        return []

    def splitlines(self, keepends=False): # real signature unknown; restored from __doc__
        """
        S.splitlines(keepends=False) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> string or unicode
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        If chars is unicode, S will be converted to unicode before stripping
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> string
        
        Return a copy of the string S with uppercase characters
        converted to lowercase and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> string
        
        Return a titlecased version of S, i.e. words start with uppercase
        characters, all remaining cased characters have lowercase.
        """
        return ""

    def translate(self, table, deletechars=None): # real signature unknown; restored from __doc__
        """
        S.translate(table [,deletechars]) -> string
        
        Return a copy of the string S, where all characters occurring
        in the optional argument deletechars are removed, and the
        remaining characters have been mapped through the given
        translation table, which must be a string of length 256 or None.
        If the table argument is None, no translation is applied and
        the operation simply removes the characters in deletechars.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> string
        
        Return a copy of the string S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> string
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width.  The string S is never truncated.
        """
        return ""

    def _formatter_field_name_split(self, *args, **kwargs): # real signature unknown
        pass

    def _formatter_parser(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> string
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
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

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class _QhullUser(object):
    """ Takes care of basic dealings with the Qhull objects """
    def add_points(self, points, restart=False): # real signature unknown; restored from __doc__
        """
        add_points(points, restart=False)
        
                Process a set of additional new points.
        
                Parameters
                ----------
                points : ndarray
                    New points to add. The dimensionality should match that of the
                    initial points.
                restart : bool, optional
                    Whether to restart processing from scratch, rather than
                    adding points incrementally.
        
                Raises
                ------
                QhullError
                    Raised when Qhull encounters an error condition, such as
                    geometrical degeneracy when options to resolve are not enabled.
        
                See Also
                --------
                close
        
                Notes
                -----
                You need to specify ``incremental=True`` when constructing the
                object to be able to add points incrementally. Incremental addition
                of points is also not possible after `close` has been called.
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
                Finish incremental processing.
        
                Call this to free resources taken up by Qhull, when using the
                incremental mode. After calling this, adding more points is no
                longer possible.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _qhull = None
    __dict__ = None # (!) real value is ''
    __qualname__ = '_QhullUser'


class ConvexHull(_QhullUser):
    """
    ConvexHull(points, incremental=False, qhull_options=None)
    
        Convex hulls in N dimensions.
    
        .. versionadded:: 0.12.0
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to construct a convex hull from
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qx" for ndim > 4 and "" otherwise)
            Option "Qt" is always enabled.
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        vertices : ndarray of ints, shape (nvertices,)
            Indices of points forming the vertices of the convex hull.
            For 2-D convex hulls, the vertices are in counterclockwise order.
            For other dimensions, they are in input order.
        simplices : ndarray of ints, shape (nfacet, ndim)
            Indices of points forming the simplical facets of the convex hull.
        neighbors : ndarray of ints, shape (nfacet, ndim)
            Indices of neighbor facets for each facet.
            The kth neighbor is opposite to the kth vertex.
            -1 denotes no neighbor.
        equations : ndarray of double, shape (nfacet, ndim+1)
            [normal, offset] forming the hyperplane equation of the facet
            (see [Qhull]_ documentation for more).
        coplanar : ndarray of int, shape (ncoplanar, 3)
            Indices of coplanar points and the corresponding indices of
            the nearest facets and nearest vertex indices.  Coplanar
            points are input points which were *not* included in the
            triangulation due to numerical precision issues.
    
            If option "Qc" is not specified, this list is not computed.
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
    
        Notes
        -----
        The convex hull is computed using the Qhull libary [Qhull]_.
    
        Examples
        --------
    
        Convex hull of a random set of points:
    
        >>> from scipy.spatial import ConvexHull
        >>> points = np.random.rand(30, 2)   # 30 random points in 2-D
        >>> hull = ConvexHull(points)
    
        Plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> plt.plot(points[:,0], points[:,1], 'o')
        >>> for simplex in hull.simplices:
        >>>     plt.plot(points[simplex,0], points[simplex,1], 'k-')
    
        We could also have directly used the vertices of the hull, which
        for 2-D are guaranteed to be in counterclockwise order:
    
        >>> plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
        >>> plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
        >>> plt.show()
    
        References
        ----------
        .. [Qhull] http://www.qhull.org/
    """
    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __qualname__ = 'ConvexHull'


class Delaunay(_QhullUser):
    """
    Delaunay(points, furthest_site=False, incremental=False, qhull_options=None)
    
        Delaunay tesselation in N dimensions.
    
        .. versionadded:: 0.9
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to triangulate
        furthest_site : bool, optional
            Whether to compute a furthest-site Delaunay triangulation.
            Default: False
    
            .. versionadded:: 0.12.0
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual for
            details. Option "Qt" is always enabled.
            Default:"Qbb Qc Qz Qx" for ndim > 4 and "Qbb Qc Qz" otherwise.
            Incremental mode omits "Qz".
    
            .. versionadded:: 0.12.0
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        simplices : ndarray of ints, shape (nsimplex, ndim+1)
            Indices of the points forming the simplices in the triangulation.
        neighbors : ndarray of ints, shape (nsimplex, ndim+1)
            Indices of neighbor simplices for each simplex.
            The kth neighbor is opposite to the kth vertex.
            For simplices at the boundary, -1 denotes no neighbor.
        equations : ndarray of double, shape (nsimplex, ndim+2)
            [normal, offset] forming the hyperplane equation of the facet
            on the paraboloid (see [Qhull]_ documentation for more).
        paraboloid_scale, paraboloid_shift : float
            Scale and shift for the extra paraboloid dimension
            (see [Qhull]_ documentation for more).
        transform : ndarray of double, shape (nsimplex, ndim+1, ndim)
            Affine transform from ``x`` to the barycentric coordinates ``c``.
            This is defined by::
    
                T c = x - r
    
            At vertex ``j``, ``c_j = 1`` and the other coordinates zero.
    
            For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains
            inverse of the matrix ``T``, and ``transform[i,ndim,:]``
            contains the vector ``r``.
    
            If the simplex is degenerate or nearly degenerate, its
            barycentric transform contains NaNs.
        vertex_to_simplex : ndarray of int, shape (npoints,)
            Lookup array, from a vertex, to some simplex which it is a part of.
            If qhull option "Qc" was not specified, the list will contain -1
            for points that are not vertices of the tesselation.
        convex_hull : ndarray of int, shape (nfaces, ndim)
            Vertices of facets forming the convex hull of the point set.
            The array contains the indices of the points belonging to
            the (N-1)-dimensional facets that form the convex hull
            of the triangulation.
    
            .. note::
    
               Computing convex hulls via the Delaunay triangulation is
               inefficient and subject to increased numerical instability.
               Use `ConvexHull` instead.
        coplanar : ndarray of int, shape (ncoplanar, 3)
            Indices of coplanar points and the corresponding indices of
            the nearest facet and the nearest vertex.  Coplanar
            points are input points which were *not* included in the
            triangulation due to numerical precision issues.
    
            If option "Qc" is not specified, this list is not computed.
    
            .. versionadded:: 0.12.0
        vertices
            Same as `simplices`, but deprecated.
        vertex_neighbor_vertices : tuple of two ndarrays of int; (indices, indptr)
            Neighboring vertices of vertices. The indices of neighboring
            vertices of vertex `k` are ``indptr[indices[k]:indices[k+1]]``.
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
    
        Notes
        -----
        The tesselation is computed using the Qhull library [Qhull]_.
    
        .. note::
    
           Unless you pass in the Qhull option "QJ", Qhull does not
           guarantee that each input point appears as a vertex in the
           Delaunay triangulation. Omitted points are listed in the
           `coplanar` attribute.
    
        Examples
        --------
        Triangulation of a set of points:
    
        >>> points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
        >>> from scipy.spatial import Delaunay
        >>> tri = Delaunay(points)
    
        We can plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
        >>> plt.plot(points[:,0], points[:,1], 'o')
        >>> plt.show()
    
        Point indices and coordinates for the two triangles forming the
        triangulation:
    
        >>> tri.simplices
        array([[3, 2, 0],
               [3, 1, 0]], dtype=int32)
        >>> points[tri.simplices]
        array([[[ 1. ,  1. ],
                [ 1. ,  0. ],
                [ 0. ,  0. ]],
               [[ 1. ,  1. ],
                [ 0. ,  1.1],
                [ 0. ,  0. ]]])
    
        Triangle 0 is the only neighbor of triangle 1, and it's opposite to
        vertex 1 of triangle 1:
    
        >>> tri.neighbors[1]
        array([-1,  0, -1], dtype=int32)
        >>> points[tri.simplices[1,1]]
        array([ 0. ,  1.1])
    
        We can find out which triangle points are in:
    
        >>> p = np.array([(0.1, 0.2), (1.5, 0.5)])
        >>> tri.find_simplex(p)
        array([ 1, -1], dtype=int32)
    
        We can also compute barycentric coordinates in triangle 1 for
        these points:
    
        >>> b = tri.transform[1,:2].dot(p - tri.transform[1,2])
        >>> np.c_[b, 1 - b.sum(axis=1)]
        array([[ 0.1       ,  0.2       ,  0.7       ],
               [ 1.27272727,  0.27272727, -0.54545455]])
    
        The coordinates for the first point are all positive, meaning it
        is indeed inside the triangle.
    
        References
        ----------
        .. [Qhull] http://www.qhull.org/
    """
    def find_simplex(self, xi, bruteforce=False, tol=None): # real signature unknown; restored from __doc__
        """
        find_simplex(self, xi, bruteforce=False, tol=None)
        
                Find the simplices containing the given points.
        
                Parameters
                ----------
                tri : DelaunayInfo
                    Delaunay triangulation
                xi : ndarray of double, shape (..., ndim)
                    Points to locate
                bruteforce : bool, optional
                    Whether to only perform a brute-force search
                tol : float, optional
                    Tolerance allowed in the inside-triangle check.
                    Default is ``100*eps``.
        
                Returns
                -------
                i : ndarray of int, same shape as `xi`
                    Indices of simplices containing each point.
                    Points outside the triangulation get the value -1.
        
                Notes
                -----
                This uses an algorithm adapted from Qhull's ``qh_findbestfacet``,
                which makes use of the connection between a convex hull and a
                Delaunay triangulation. After finding the simplex closest to
                the point in N+1 dimensions, the algorithm falls back to
                directed search in N dimensions.
        """
        pass

    def lift_points(self, x): # real signature unknown; restored from __doc__
        """
        lift_points(self, x)
        
                Lift points to the Qhull paraboloid.
        """
        pass

    def plane_distance(self, xi): # real signature unknown; restored from __doc__
        """
        plane_distance(self, xi)
        
                Compute hyperplane distances to the point `xi` from all simplices.
        """
        pass

    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    convex_hull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Vertices of facets forming the convex hull of the point set.

        :type: ndarray of int, shape (nfaces, ndim)

        The array contains the indices of the points
        belonging to the (N-1)-dimensional facets that form the convex
        hull of the triangulation.

        .. note::

           Computing convex hulls via the Delaunay triangulation is
           inefficient and subject to increased numerical instability.
           Use `ConvexHull` instead.

        """

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Affine transform from ``x`` to the barycentric coordinates ``c``.

        :type: ndarray of double, shape (nsimplex, ndim+1, ndim)

        This is defined by::

            T c = x - r

        At vertex ``j``, ``c_j = 1`` and the other coordinates zero.

        For simplex ``i``, ``transform[i,:ndim,:ndim]`` contains
        inverse of the matrix ``T``, and ``transform[i,ndim,:]``
        contains the vector ``r``.

        """

    vertex_neighbor_vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Neighboring vertices of vertices.

        Tuple of two ndarrays of int: (indices, indptr). The indices of
        neighboring vertices of vertex `k` are
        ``indptr[indices[k]:indices[k+1]]``.

        """

    vertex_to_simplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Lookup array, from a vertex, to some simplex which it is a part of.

        :type: ndarray of int, shape (npoints,)
        """


    __qualname__ = 'Delaunay'


class QhullError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'QhullError'


class Voronoi(_QhullUser):
    """
    Voronoi(points, furthest_site=False, incremental=False, qhull_options=None)
    
        Voronoi diagrams in N dimensions.
    
        .. versionadded:: 0.12.0
    
        Parameters
        ----------
        points : ndarray of floats, shape (npoints, ndim)
            Coordinates of points to construct a convex hull from
        furthest_site : bool, optional
            Whether to compute a furthest-site Voronoi diagram. Default: False
        incremental : bool, optional
            Allow adding new points incrementally. This takes up some additional
            resources.
        qhull_options : str, optional
            Additional options to pass to Qhull. See Qhull manual
            for details. (Default: "Qbb Qc Qz Qx" for ndim > 4 and
            "Qbb Qc Qz" otherwise. Incremental mode omits "Qz".)
    
        Attributes
        ----------
        points : ndarray of double, shape (npoints, ndim)
            Coordinates of input points.
        vertices : ndarray of double, shape (nvertices, ndim)
            Coordinates of the Voronoi vertices.
        ridge_points : ndarray of ints, shape (nridges, 2)
            Indices of the points between which each Voronoi ridge lies.
        ridge_vertices : list of list of ints, shape (nridges, *)
            Indices of the Voronoi vertices forming each Voronoi ridge.
        regions : list of list of ints, shape (nregions, *)
            Indices of the Voronoi vertices forming each Voronoi region.
            -1 indicates vertex outside the Voronoi diagram.
        point_region : list of ints, shape (npoints)
            Index of the Voronoi region for each input point.
            If qhull option "Qc" was not specified, the list will contain -1
            for points that are not associated with a Voronoi region.
    
        Raises
        ------
        QhullError
            Raised when Qhull encounters an error condition, such as
            geometrical degeneracy when options to resolve are not enabled.
    
        Notes
        -----
        The Voronoi diagram is computed using the Qhull libary [Qhull]_.
    
        Examples
        --------
        Voronoi diagram for a set of point:
    
        >>> points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
        ...                    [2, 0], [2, 1], [2, 2]])
        >>> from scipy.spatial import Voronoi, voronoi_plot_2d
        >>> vor = Voronoi(points)
    
        Plot it:
    
        >>> import matplotlib.pyplot as plt
        >>> voronoi_plot_2d(vor)
        >>> plt.show()
    
        The Voronoi vertices:
    
        >>> vor.vertices
        array([[ 0.5,  0.5],
               [ 1.5,  0.5],
               [ 0.5,  1.5],
               [ 1.5,  1.5]])
    
        There is a single finite Voronoi region, and four finite Voronoi
        ridges:
    
        >>> vor.regions
        [[], [-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [3, 2, 0, 1], [2, -1, 0], [3, -1, 1]]
        >>> vor.ridge_vertices
        [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [0, 2], [1, 3]]
    
        The ridges are perpendicular between lines drawn between the following
        input points:
    
        >>> vor.ridge_points
        array([[0, 1],
               [0, 3],
               [6, 3],
               [6, 7],
               [3, 4],
               [5, 8],
               [5, 2],
               [5, 4],
               [8, 7],
               [2, 1],
               [4, 1],
               [4, 7]], dtype=int32)
    
        References
        ----------
        .. [Qhull] http://www.qhull.org/
    """
    def _update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ridge_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __qualname__ = 'Voronoi'


class _Qhull(object):
    # no doc
    def add_points(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def get_extremes_2d(self, *args, **kwargs): # real signature unknown
        pass

    def get_paraboloid_shift_scale(self, *args, **kwargs): # real signature unknown
        pass

    def get_points(self, *args, **kwargs): # real signature unknown
        pass

    def get_simplex_facet_array(self, *args, **kwargs): # real signature unknown
        pass

    def get_voronoi_diagram(self, *args, **kwargs): # real signature unknown
        pass

    def triangulate(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    furthest_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode_option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

_qhull_lock = None # (!) real value is ''

__all__ = [
    'Delaunay',
    'ConvexHull',
    'Voronoi',
    'tsearch',
]

__pyx_capi__ = {
    '_barycentric_coordinate_single': None, # (!) real value is ''
    '_barycentric_coordinates': None, # (!) real value is ''
    '_barycentric_inside': None, # (!) real value is ''
    '_distplane': None, # (!) real value is ''
    '_find_simplex': None, # (!) real value is ''
    '_find_simplex_bruteforce': None, # (!) real value is ''
    '_find_simplex_directed': None, # (!) real value is ''
    '_get_delaunay_info': None, # (!) real value is ''
    '_is_point_fully_outside': None, # (!) real value is ''
    '_lift_point': None, # (!) real value is ''
}

__test__ = {}

