# encoding: utf-8
# module scipy.spatial.ckdtree
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/spatial/ckdtree.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import scipy as scipy # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/__init__.pyc
import numpy as np # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.pyc

# no functions
# classes

class cKDTree(object):
    """
    cKDTree(data, int leafsize=10)
    
        kd-tree for quick nearest-neighbor lookup
    
        This class provides an index into a set of k-dimensional points
        which can be used to rapidly look up the nearest neighbors of any
        point. 
    
        The algorithm used is described in Maneewongvatana and Mount 1999. 
        The general idea is that the kd-tree is a binary trie, each of whose
        nodes represents an axis-aligned hyperrectangle. Each node specifies
        an axis and splits the set of points based on whether their coordinate
        along that axis is greater than or less than a particular value. 
    
        During construction, the axis and splitting point are chosen by the 
        "sliding midpoint" rule, which ensures that the cells do not all
        become long and thin. 
    
        The tree can be queried for the r closest neighbors of any given point 
        (optionally returning only those within some maximum distance of the 
        point). It can also be queried, with a substantial gain in efficiency, 
        for the r approximate closest neighbors.
    
        For large dimensions (20 is already large) do not expect this to run 
        significantly faster than brute force. High-dimensional nearest-neighbor
        queries are a substantial open problem in computer science.
    
        Parameters
        ----------
        data : array-like, shape (n,m)
            The n data points of dimension mto be indexed. This array is 
            not copied unless this is necessary to produce a contiguous 
            array of doubles, and so modifying this data will result in 
            bogus results.
        leafsize : positive integer
            The number of points at which the algorithm switches over to
            brute-force.
    """
    def count_neighbors(self, other, r, p): # real signature unknown; restored from __doc__
        """
        count_neighbors(self, other, r, p)
        
                Count how many nearby pairs can be formed.
        
                Count the number of pairs (x1,x2) can be formed, with x1 drawn
                from self and x2 drawn from `other`, and where
                ``distance(x1, x2, p) <= r``.
                This is the "two-point correlation" described in Gray and Moore 2000,
                "N-body problems in statistical learning", and the code here is based
                on their algorithm.
        
                Parameters
                ----------
                other : KDTree instance
                    The other tree to draw points from.
                r : float or one-dimensional array of floats
                    The radius to produce a count for. Multiple radii are searched with
                    a single tree traversal.
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use
        
                Returns
                -------
                result : int or 1-D array of ints
                    The number of pairs. Note that this is internally stored in a numpy int,
                    and so may overflow if very large (2e9).
        """
        pass

    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=None): # real signature unknown; restored from __doc__
        """
        query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf)
                
                Query the kd-tree for nearest neighbors
        
                Parameters
                ----------
                x : array_like, last dimension self.m
                    An array of points to query.
                k : integer
                    The number of nearest neighbors to return.
                eps : non-negative float
                    Return approximate nearest neighbors; the kth returned value 
                    is guaranteed to be no further than (1+eps) times the 
                    distance to the real k-th nearest neighbor.
                p : float, 1<=p<=infinity
                    Which Minkowski p-norm to use. 
                    1 is the sum-of-absolute-values "Manhattan" distance
                    2 is the usual Euclidean distance
                    infinity is the maximum-coordinate-difference distance
                distance_upper_bound : nonnegative float
                    Return only neighbors within this distance.  This is used to prune
                    tree searches, so if you are doing a series of nearest-neighbor
                    queries, it may help to supply the distance to the nearest neighbor
                    of the most recent point.
        
                Returns
                -------
                d : array of floats
                    The distances to the nearest neighbors. 
                    If x has shape tuple+(self.m,), then d has shape tuple+(k,).
                    Missing neighbors are indicated with infinite distances.
                i : ndarray of ints
                    The locations of the neighbors in self.data.
                    If `x` has shape tuple+(self.m,), then `i` has shape tuple+(k,).
                    Missing neighbors are indicated with self.n.
        """
        pass

    def query_ball_point(self, x, r, p, eps): # real signature unknown; restored from __doc__
        """
        query_ball_point(self, x, r, p, eps)
                
                Find all points within distance r of point(s) x.
        
                Parameters
                ----------
                x : array_like, shape tuple + (self.m,)
                    The point or points to search for neighbors of.
                r : positive float
                    The radius of points to return.
                p : float, optional
                    Which Minkowski p-norm to use.  Should be in the range [1, inf].
                eps : nonnegative float, optional
                    Approximate search. Branches of the tree are not explored if their
                    nearest points are further than ``r / (1 + eps)``, and branches are
                    added in bulk if their furthest points are nearer than
                    ``r * (1 + eps)``.
        
                Returns
                -------
                results : list or array of lists
                    If `x` is a single point, returns a list of the indices of the
                    neighbors of `x`. If `x` is an array of points, returns an object
                    array of shape tuple containing lists of neighbors.
        
                Notes
                -----
                If you have many points whose neighbors you want to find, you may save
                substantial amounts of time by putting them in a cKDTree and using
                query_ball_tree.
        
                Examples
                --------
                >>> from scipy import spatial
                >>> x, y = np.mgrid[0:4, 0:4]
                >>> points = zip(x.ravel(), y.ravel())
                >>> tree = spatial.cKDTree(points)
                >>> tree.query_ball_point([2, 0], 1)
                [4, 8, 9, 12]
        """
        pass

    def query_ball_tree(self, other, r, p, eps): # real signature unknown; restored from __doc__
        """
        query_ball_tree(self, other, r, p, eps)
        
                Find all pairs of points whose distance is at most r
        
                Parameters
                ----------
                other : KDTree instance
                    The tree containing points to search against.
                r : float
                    The maximum distance, has to be positive.
                p : float, optional
                    Which Minkowski norm to use.  `p` has to meet the condition
                    ``1 <= p <= infinity``.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
        
                Returns
                -------
                results : list of lists
                    For each element ``self.data[i]`` of this tree, ``results[i]`` is a
                    list of the indices of its neighbors in ``other.data``.
        """
        pass

    def query_pairs(self, r, p, eps): # real signature unknown; restored from __doc__
        """
        query_pairs(self, r, p, eps)
        
                Find all pairs of points whose distance is at most r.
        
                Parameters
                ----------
                r : positive float
                    The maximum distance.
                p : float, optional
                    Which Minkowski norm to use.  `p` has to meet the condition
                    ``1 <= p <= infinity``.
                eps : float, optional
                    Approximate search.  Branches of the tree are not explored
                    if their nearest points are further than ``r/(1+eps)``, and
                    branches are added in bulk if their furthest points are nearer
                    than ``r * (1+eps)``.  `eps` has to be non-negative.
        
                Returns
                -------
                results : set
                    Set of pairs ``(i,j)``, with ``i < j`, for which the corresponding
                    positions are close.
        """
        pass

    def sparse_distance_matrix(self, max_distance, p): # real signature unknown; restored from __doc__
        """
        sparse_distance_matrix(self, max_distance, p)
        
                Compute a sparse distance matrix
        
                Computes a distance matrix between two KDTrees, leaving as zero
                any distance greater than max_distance.
        
                Parameters
                ----------
                other : cKDTree
        
                max_distance : positive float
        
                Returns
                -------
                result : dok_matrix
                    Sparse matrix representing the results in "dictionary of keys" format.
                    FIXME: Internally, built as a COO matrix, it would be more
                    efficient to return this COO matrix.
        """
        pass

    def __init__(self, data, int_leafsize=10): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leafsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class coo_entries(object):
    # no doc
    def to_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class heap(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class PointRectDistanceTracker(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


class Rectangle(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class RectRectDistanceTracker(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


# variables with complex values

__all__ = [
    'cKDTree',
]

__test__ = {
    u'cKDTree.query_ball_point (line 1343)': u'query_ball_point(self, x, r, p, eps)\n        \n        Find all points within distance r of point(s) x.\n\n        Parameters\n        ----------\n        x : array_like, shape tuple + (self.m,)\n            The point or points to search for neighbors of.\n        r : positive float\n            The radius of points to return.\n        p : float, optional\n            Which Minkowski p-norm to use.  Should be in the range [1, inf].\n        eps : nonnegative float, optional\n            Approximate search. Branches of the tree are not explored if their\n            nearest points are further than ``r / (1 + eps)``, and branches are\n            added in bulk if their furthest points are nearer than\n            ``r * (1 + eps)``.\n\n        Returns\n        -------\n        results : list or array of lists\n            If `x` is a single point, returns a list of the indices of the\n            neighbors of `x`. If `x` is an array of points, returns an object\n            array of shape tuple containing lists of neighbors.\n\n        Notes\n        -----\n        If you have many points whose neighbors you want to find, you may save\n        substantial amounts of time by putting them in a cKDTree and using\n        query_ball_tree.\n\n        Examples\n        --------\n        >>> from scipy import spatial\n        >>> x, y = np.mgrid[0:4, 0:4]\n        >>> points = zip(x.ravel(), y.ravel())\n        >>> tree = spatial.cKDTree(points)\n        >>> tree.query_ball_point([2, 0], 1)\n        [4, 8, 9, 12]\n\n        ',
}

