# encoding: utf-8
# module scipy.sparse.csgraph._shortest_path
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/sparse/csgraph/_shortest_path.so
# by generator 1.136
"""
Routines for performing shortest-path graph searches

The main interface is in the function :func:`shortest_path`.  This
calls cython routines that compute the shortest path using
the Floyd-Warshall algorithm, Dijkstra's algorithm with Fibonacci Heaps,
the Bellman-Ford algorithm, or Johnson's Algorithm.
"""

# imports
import warnings as warnings # /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/warnings.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.pyc
import numpy as __numpy
import scipy.sparse.compressed as __scipy_sparse_compressed
import scipy.sparse.sputils as __scipy_sparse_sputils


# functions

def bellman_ford(csgraph, directed=True, indices=None, return_predecessors=False, unweighted=False): # real signature unknown; restored from __doc__
    """
    bellman_ford(csgraph, directed=True, indices=None, return_predecessors=False,
                     unweighted=False)
    
        Compute the shortest path lengths using the Bellman-Ford algorithm.
        
        The Bellman-ford algorithm can robustly deal with graphs with negative
        weights.  If a negative cycle is detected, an error is raised.  For
        graphs without negative edge weights, dijkstra's algorithm may be faster.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        indices : array_like or int, optional
            if specified, only compute the paths for the points at the given
            indices.
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    
        Notes
        -----
        This routine is specially designed for graphs with negative edge weights.
        If all edge weights are positive, then Dijkstra's algorithm is a better
        choice.
    """
    pass

def dijkstra(csgraph, directed=True, indices=None, return_predecessors=False, unweighted=False): # real signature unknown; restored from __doc__
    """
    dijkstra(csgraph, directed=True, indices=None, return_predecessors=False,
                 unweighted=False)
    
        Dijkstra algorithm using Fibonacci Heaps
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of non-negative distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        indices : array_like or int, optional
            if specified, only compute the paths for the points at the given
            indices.
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
    
        Returns
        -------
        dist_matrix : ndarray
            The matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Notes
        -----
        As currently implemented, Dijkstra's algorithm does not work for
        graphs with direction-dependent distances when directed == False.
        i.e., if csgraph[i,j] and csgraph[j,i] are not equal and
        both are nonzero, setting directed=False will not yield the correct
        result.
    
        Also, this routine does not work for graphs with negative
        distances.  Negative distances can lead to infinite cycles that must
        be handled by specialized algorithms such as Bellman-Ford's algorithm
        or Johnson's algorithm.
    """
    pass

def floyd_warshall(csgraph, directed=True, return_predecessors=False, unweighted=False, overwrite=False): # real signature unknown; restored from __doc__
    """
    floyd_warshall(csgraph, directed=True, return_predecessors=False,
                       unweighted=False, overwrite=False)
    
        Compute the shortest path lengths using the Floyd-Warshall algorithm
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
        overwrite : bool, optional
            If True, overwrite csgraph with the result.  This applies only if
            csgraph is a dense, c-ordered array with dtype=float64.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    """
    pass

def isspmatrix(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    # no doc
    pass

def johnson(csgraph, directed=True, indices=None, return_predecessors=False, unweighted=False): # real signature unknown; restored from __doc__
    """
    johnson(csgraph, directed=True, indices=None, return_predecessors=False,
                unweighted=False)
    
        Compute the shortest path lengths using Johnson's algorithm.
    
        Johnson's algorithm combines the Bellman-Ford algorithm and Dijkstra's
        algorithm to quickly find shortest paths in a way that is robust to
        the presence of negative cycles.  If a negative cycle is detected,
        an error is raised.  For graphs without negative edge weights,
        dijkstra() may be faster.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        indices : array_like or int, optional
            if specified, only compute the paths for the points at the given
            indices.
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    
        Notes
        -----
        This routine is specially designed for graphs with negative edge weights.
        If all edge weights are positive, then Dijkstra's algorithm is a better
        choice.
    """
    pass

def shortest_path(csgraph, method='auto', directed=True, return_predecessors=False, unweighted=False, overwrite=False): # real signature unknown; restored from __doc__
    """
    shortest_path(csgraph, method='auto', directed=True, return_predecessors=False,
                      unweighted=False, overwrite=False)
    
        Perform a shortest-path graph search on a positive directed or
        undirected graph.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array, matrix, or sparse matrix, 2 dimensions
            The N x N array of distances representing the input graph.
        method : string ['auto'|'FW'|'D'], optional
            Algorithm to use for shortest paths.  Options are:
            
               'auto' -- (default) select the best among 'FW', 'D', 'BF', or 'J' 
                         based on the input data.
    
               'FW'   -- Floyd-Warshall algorithm.  Computational cost is
                         approximately ``O[N^3]``.  The input csgraph will be
                         converted to a dense representation.
    
               'D'    -- Dijkstra's algorithm with Fibonacci heaps.  Computational
                         cost is approximately ``O[N(N*k + N*log(N))]``, where
    		     ``k`` is the average number of connected edges per node.
    		     The input csgraph will be converted to a csr
    		     representation.
    
               'BF'   -- Bellman-Ford algorithm.  This algorithm can be used when
                         weights are negative.  If a negative cycle is encountered,
                         an error will be raised.  Computational cost is
                         approximately ``O[N(N^2 k)]``, where ``k`` is the average
                         number of connected edges per node. The input csgraph will
                         be converted to a csr representation.
    
               'J'    -- Johnson's algorithm.  Like the Bellman-Ford algorithm,
                         Johnson's algorithm is designed for use when the weights
                         are negative.  It combines the Bellman-Ford algorithm
                         with Dijkstra's algorithm for faster computation.
    
        directed : bool, optional
            If True (default), then find the shortest path on a directed graph:
            only move from point i to point j along paths csgraph[i, j].
            If False, then find the shortest path on an undirected graph: the
            algorithm can progress from point i to j along csgraph[i, j] or
            csgraph[j, i]
        return_predecessors : bool, optional
            If True, return the size (N, N) predecesor matrix
        unweighted : bool, optional
            If True, then find unweighted distances.  That is, rather than finding
            the path between each point such that the sum of weights is minimized,
            find the path such that the number of edges is minimized.
        overwrite : bool, optional
            If True, overwrite csgraph with the result.  This applies only if
            method == 'FW' and csgraph is a dense, c-ordered array with
            dtype=float64.
    
        Returns
        -------
        dist_matrix : ndarray
            The N x N matrix of distances between graph nodes. dist_matrix[i,j]
            gives the shortest distance from point i to point j along the graph.
    
        predecessors : ndarray
            Returned only if return_predecessors == True.
            The N x N matrix of predecessors, which can be used to reconstruct
            the shortest paths.  Row i of the predecessor matrix contains
            information on the shortest paths from point i: each entry
            predecessors[i, j] gives the index of the previous node in the
            path from point i to point j.  If no path exists between point
            i and j, then predecessors[i, j] = -9999
    
        Raises
        ------
        NegativeCycleError:
            if there are negative cycles in the graph
    
        Notes
        -----
        As currently implemented, Dijkstra's algorithm and Johnson's algorithm
        do not work for graphs with direction-dependent distances when
        directed == False.  i.e., if csgraph[i,j] and csgraph[j,i] are non-equal
        edges, method='D' may yield an incorrect result.
    """
    pass

def validate_graph(csgraph, directed, dtype="<type 'numpy.float64'>", csr_output=True, dense_output=True, copy_if_dense=False, copy_if_sparse=False, null_value_in=0, null_value_out=inf, infinity_null=True, nan_null=True): # reliably restored by inspect
    """ Routine for validation and conversion of csgraph inputs """
    pass

# classes

class csr_matrix(__scipy_sparse_compressed._cs_matrix, __scipy_sparse_sputils.IndexMixin):
    """
    Compressed Sparse Row matrix
    
        This can be instantiated in several ways:
            csr_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csr_matrix(S)
                with another sparse matrix S (equivalent to S.tocsr())
    
            csr_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csr_matrix((data, ij), [shape=(M, N)])
                where ``data`` and ``ij`` satisfy the relationship
                ``a[ij[0, k], ij[1, k]] = data[k]``
    
            csr_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSR representation where the column indices for
                row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
                corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
                If the shape parameter is not supplied, the matrix dimensions
                are inferred from the index arrays.
    
        Attributes
        ----------
        dtype : dtype
            Data type of the matrix
        shape : 2-tuple
            Shape of the matrix
        ndim : int
            Number of dimensions (this is always 2)
        nnz
            Number of nonzero elements
        data
            CSR format data array of the matrix
        indices
            CSR format index array of the matrix
        indptr
            CSR format index pointer array of the matrix
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSR format
          - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
          - efficient row slicing
          - fast matrix vector products
    
        Disadvantages of the CSR format
          - slow column slicing operations (consider CSC)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
        Examples
        --------
    
        >>> from scipy.sparse import *
        >>> from scipy import *
        >>> csr_matrix( (3,4), dtype=int8 ).todense()
        matrix([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]], dtype=int8)
    
        >>> row = array([0,0,1,2,2,2])
        >>> col = array([0,2,2,0,1,2])
        >>> data = array([1,2,3,4,5,6])
        >>> csr_matrix( (data,(row,col)), shape=(3,3) ).todense()
        matrix([[1, 0, 2],
                [0, 0, 3],
                [4, 5, 6]])
    
        >>> indptr = array([0,2,3,6])
        >>> indices = array([0,2,2,0,1,2])
        >>> data = array([1,2,3,4,5,6])
        >>> csr_matrix( (data,indices,indptr), shape=(3,3) ).todense()
        matrix([[1, 0, 2],
                [0, 0, 3],
                [4, 5, 6]])
    """
    def getcol(self, *args, **kwargs): # real signature unknown
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSR matrix (column vector).
        """
        pass

    def getrow(self, *args, **kwargs): # real signature unknown
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def tobsr(self, *args, **kwargs): # real signature unknown
        pass

    def tocsc(self, *args, **kwargs): # real signature unknown
        pass

    def tocsr(self, *args, **kwargs): # real signature unknown
        pass

    def tolil(self, *args, **kwargs): # real signature unknown
        pass

    def transpose(self, *args, **kwargs): # real signature unknown
        pass

    def _get_row_slice(self, *args, **kwargs): # real signature unknown
        """ Returns a copy of row self[i, cslice] """
        pass

    def _get_single_element(self, *args, **kwargs): # real signature unknown
        """ Returns the single element self[row, col] """
        pass

    def _get_submatrix(self, *args, **kwargs): # real signature unknown
        """ Return a submatrix of this matrix (new matrix is created). """
        pass

    def _swap(self, *args, **kwargs): # real signature unknown
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class DTYPE(__numpy.floating, float):
    """ 64-bit floating-point number. Character code 'd'. Python float compatible. """
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class ITYPE(__numpy.signedinteger):
    """ 32-bit integer. Character code 'i'. C int compatible. """
    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
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

    def __index__(self): # real signature unknown; restored from __doc__
        """ x[y:z] <==> x[y.__index__():z.__index__()] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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


class NegativeCycleError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __qualname__ = 'NegativeCycleError'


# variables with complex values

__test__ = {}

