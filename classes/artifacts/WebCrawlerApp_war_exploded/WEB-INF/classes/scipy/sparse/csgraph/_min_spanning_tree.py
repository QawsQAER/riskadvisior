# encoding: utf-8
# module scipy.sparse.csgraph._min_spanning_tree
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/sparse/csgraph/_min_spanning_tree.so
# by generator 1.136
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.pyc
import numpy as __numpy
import scipy.sparse.compressed as __scipy_sparse_compressed
import scipy.sparse.sputils as __scipy_sparse_sputils


# functions

def isspmatrix(x): # reliably restored by inspect
    # no doc
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    # no doc
    pass

def minimum_spanning_tree(csgraph, overwrite=False): # real signature unknown; restored from __doc__
    """
    minimum_spanning_tree(csgraph, overwrite=False)
    
        Return a minimum spanning tree of an undirected graph
    
        A minimum spanning tree is a graph consisting of the subset of edges
        which together connect all connected nodes, while minimizing the total
        sum of weights on the edges.  This is computed using the Kruskal algorithm.
    
        .. versionadded:: 0.11.0
    
        Parameters
        ----------
        csgraph : array_like or sparse matrix, 2 dimensions
            The N x N matrix representing an undirected graph over N nodes
            (see notes below).
        overwrite : bool, optional
            if true, then parts of the input graph will be overwritten for
            efficiency.
    
        Returns
        -------
        span_tree : csr matrix
            The N x N compressed-sparse representation of the undirected minimum
            spanning tree over the input (see notes below).
    
        Notes
        -----
        This routine uses undirected graphs as input and output.  That is, if
        graph[i, j] and graph[j, i] are both zero, then nodes i and j do not
        have an edge connecting them.  If either is nonzero, then the two are
        connected by the minimum nonzero value of the two.
    
        Examples
        --------
        The following example shows the computation of a minimum spanning tree
        over a simple four-component graph::
    
             input graph             minimum spanning tree
    
                 (0)                         (0)
                /   \                       /
               3     8                     3
              /       \                   /
            (3)---5---(1)               (3)---5---(1)
              \       /                           /
               6     2                           2
                \   /                           /
                 (2)                         (2)
    
        It is easy to see from inspection that the minimum spanning tree involves
        removing the edges with weights 8 and 6.  In compressed sparse
        representation, the solution looks like this:
    
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import minimum_spanning_tree
        >>> X = csr_matrix([[0, 8, 0, 3],
        ...                 [0, 0, 2, 5],
        ...                 [0, 0, 0, 6],
        ...                 [0, 0, 0, 0]])
        >>> Tcsr = minimum_spanning_tree(X)
        >>> Tcsr.toarray().astype(int)
        array([[0, 0, 0, 3],
               [0, 0, 2, 5],
               [0, 0, 0, 0],
               [0, 0, 0, 0]])
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


# variables with complex values

__test__ = {
    u'minimum_spanning_tree (line 12)': u'\n    minimum_spanning_tree(csgraph, overwrite=False)\n\n    Return a minimum spanning tree of an undirected graph\n\n    A minimum spanning tree is a graph consisting of the subset of edges\n    which together connect all connected nodes, while minimizing the total\n    sum of weights on the edges.  This is computed using the Kruskal algorithm.\n\n    .. versionadded:: 0.11.0\n\n    Parameters\n    ----------\n    csgraph : array_like or sparse matrix, 2 dimensions\n        The N x N matrix representing an undirected graph over N nodes\n        (see notes below).\n    overwrite : bool, optional\n        if true, then parts of the input graph will be overwritten for\n        efficiency.\n\n    Returns\n    -------\n    span_tree : csr matrix\n        The N x N compressed-sparse representation of the undirected minimum\n        spanning tree over the input (see notes below).\n\n    Notes\n    -----\n    This routine uses undirected graphs as input and output.  That is, if\n    graph[i, j] and graph[j, i] are both zero, then nodes i and j do not\n    have an edge connecting them.  If either is nonzero, then the two are\n    connected by the minimum nonzero value of the two.\n\n    Examples\n    --------\n    The following example shows the computation of a minimum spanning tree\n    over a simple four-component graph::\n\n         input graph             minimum spanning tree\n\n             (0)                         (0)\n            /   \\                       /\n           3     8                     3\n          /       \\                   /\n        (3)---5---(1)               (3)---5---(1)\n          \\       /                           /\n           6     2                           2\n            \\   /                           /\n             (2)                         (2)\n\n    It is easy to see from inspection that the minimum spanning tree involves\n    removing the edges with weights 8 and 6.  In compressed sparse\n    representation, the solution looks like this:\n\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import minimum_spanning_tree\n    >>> X = csr_matrix([[0, 8, 0, 3],\n    ...                 [0, 0, 2, 5],\n    ...                 [0, 0, 0, 6],\n    ...                 [0, 0, 0, 0]])\n    >>> Tcsr = minimum_spanning_tree(X)\n    >>> Tcsr.toarray().astype(int)\n    array([[0, 0, 0, 3],\n           [0, 0, 2, 5],\n           [0, 0, 0, 0],\n           [0, 0, 0, 0]])\n    ',
}

