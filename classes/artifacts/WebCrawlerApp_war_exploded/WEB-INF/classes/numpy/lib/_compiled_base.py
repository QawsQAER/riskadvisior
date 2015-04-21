# encoding: utf-8
# module numpy.lib._compiled_base
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/lib/_compiled_base.so
# by generator 1.136
# no doc

# imports
from exceptions import error


# functions

def add_docstring(obj, docstring): # real signature unknown; restored from __doc__
    """
    add_docstring(obj, docstring)
    
        Add a docstring to a built-in obj if possible.
        If the obj already has a docstring raise a RuntimeError
        If this routine does not know how to add a docstring to the object
        raise a TypeError
    """
    pass

def add_newdoc_ufunc(*args, **kwargs): # real signature unknown
    """
    add_ufunc_docstring(ufunc, new_docstring)
    
        Replace the docstring for a ufunc with new_docstring.
        This method will only work if the current docstring for
        the ufunc is NULL. (At the C level, i.e. when ufunc->doc is NULL.)
    
        Parameters
        ----------
        ufunc : numpy.ufunc
            A ufunc whose current doc is NULL.
        new_docstring : string
            The new docstring for the ufunc.
    
        Notes
        -----
        This method allocates memory for new_docstring on
        the heap. Technically this creates a mempory leak, since this
        memory will not be reclaimed until the end of the program
        even if the ufunc itself is removed. However this will only
        be a problem if the user is repeatedly creating ufuncs with
        no documentation, adding documentation via add_newdoc_ufunc,
        and then throwing away the ufunc.
    """
    pass

def bincount(x, weights=None, minlength=None): # real signature unknown; restored from __doc__
    """
    bincount(x, weights=None, minlength=None)
    
        Count number of occurrences of each value in array of non-negative ints.
    
        The number of bins (of size 1) is one larger than the largest value in
        `x`. If `minlength` is specified, there will be at least this number
        of bins in the output array (though it will be longer if necessary,
        depending on the contents of `x`).
        Each bin gives the number of occurrences of its index value in `x`.
        If `weights` is specified the input array is weighted by it, i.e. if a
        value ``n`` is found at position ``i``, ``out[n] += weight[i]`` instead
        of ``out[n] += 1``.
    
        Parameters
        ----------
        x : array_like, 1 dimension, nonnegative ints
            Input array.
        weights : array_like, optional
            Weights, array of the same shape as `x`.
        minlength : int, optional
            .. versionadded:: 1.6.0
    
            A minimum number of bins for the output array.
    
        Returns
        -------
        out : ndarray of ints
            The result of binning the input array.
            The length of `out` is equal to ``np.amax(x)+1``.
    
        Raises
        ------
        ValueError
            If the input is not 1-dimensional, or contains elements with negative
            values, or if `minlength` is non-positive.
        TypeError
            If the type of the input is float or complex.
    
        See Also
        --------
        histogram, digitize, unique
    
        Examples
        --------
        >>> np.bincount(np.arange(5))
        array([1, 1, 1, 1, 1])
        >>> np.bincount(np.array([0, 1, 1, 3, 2, 1, 7]))
        array([1, 3, 1, 1, 0, 0, 0, 1])
    
        >>> x = np.array([0, 1, 1, 3, 2, 1, 7, 23])
        >>> np.bincount(x).size == np.amax(x)+1
        True
    
        The input array needs to be of integer dtype, otherwise a
        TypeError is raised:
    
        >>> np.bincount(np.arange(5, dtype=np.float))
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: array cannot be safely cast to required type
    
        A possible use of ``bincount`` is to perform sums over
        variable-size chunks of an array, using the ``weights`` keyword.
    
        >>> w = np.array([0.3, 0.5, 0.2, 0.7, 1., -0.6]) # weights
        >>> x = np.array([0, 1, 1, 2, 2, 2])
        >>> np.bincount(x,  weights=w)
        array([ 0.3,  0.7,  1.1])
    """
    pass

def digitize(x, bins, right=False): # real signature unknown; restored from __doc__
    """
    digitize(x, bins, right=False)
    
        Return the indices of the bins to which each value in input array belongs.
    
        Each index ``i`` returned is such that ``bins[i-1] <= x < bins[i]`` if
        `bins` is monotonically increasing, or ``bins[i-1] > x >= bins[i]`` if
        `bins` is monotonically decreasing. If values in `x` are beyond the
        bounds of `bins`, 0 or ``len(bins)`` is returned as appropriate. If right
        is True, then the right bin is closed so that the index ``i`` is such
        that ``bins[i-1] < x <= bins[i]`` or bins[i-1] >= x > bins[i]`` if `bins`
        is monotonically increasing or decreasing, respectively.
    
        Parameters
        ----------
        x : array_like
            Input array to be binned. It has to be 1-dimensional.
        bins : array_like
            Array of bins. It has to be 1-dimensional and monotonic.
        right : bool, optional
            Indicating whether the intervals include the right or the left bin
            edge. Default behavior is (right==False) indicating that the interval
            does not include the right edge. The left bin and is open in this
            case. Ie., bins[i-1] <= x < bins[i] is the default behavior for
            monotonically increasing bins.
    
        Returns
        -------
        out : ndarray of ints
            Output array of indices, of same shape as `x`.
    
        Raises
        ------
        ValueError
            If the input is not 1-dimensional, or if `bins` is not monotonic.
        TypeError
            If the type of the input is complex.
    
        See Also
        --------
        bincount, histogram, unique
    
        Notes
        -----
        If values in `x` are such that they fall outside the bin range,
        attempting to index `bins` with the indices that `digitize` returns
        will result in an IndexError.
    
        Examples
        --------
        >>> x = np.array([0.2, 6.4, 3.0, 1.6])
        >>> bins = np.array([0.0, 1.0, 2.5, 4.0, 10.0])
        >>> inds = np.digitize(x, bins)
        >>> inds
        array([1, 4, 3, 2])
        >>> for n in range(x.size):
        ...   print bins[inds[n]-1], "<=", x[n], "<", bins[inds[n]]
        ...
        0.0 <= 0.2 < 1.0
        4.0 <= 6.4 < 10.0
        2.5 <= 3.0 < 4.0
        1.0 <= 1.6 < 2.5
    
        >>> x = np.array([1.2, 10.0, 12.4, 15.5, 20.])
        >>> bins = np.array([0,5,10,15,20])
        >>> np.digitize(x,bins,right=True)
        array([1, 2, 3, 4, 4])
        >>> np.digitize(x,bins,right=False)
        array([1, 3, 3, 4, 5])
    """
    pass

def interp(*args, **kwargs): # real signature unknown
    pass

def packbits(myarray, axis=None): # real signature unknown; restored from __doc__
    """
    packbits(myarray, axis=None)
    
        Packs the elements of a binary-valued array into bits in a uint8 array.
    
        The result is padded to full bytes by inserting zero bits at the end.
    
        Parameters
        ----------
        myarray : array_like
            An integer type array whose elements should be packed to bits.
        axis : int, optional
            The dimension over which bit-packing is done.
            ``None`` implies packing the flattened array.
    
        Returns
        -------
        packed : ndarray
            Array of type uint8 whose elements represent bits corresponding to the
            logical (0 or nonzero) value of the input elements. The shape of
            `packed` has the same number of dimensions as the input (unless `axis`
            is None, in which case the output is 1-D).
    
        See Also
        --------
        unpackbits: Unpacks elements of a uint8 array into a binary-valued output
                    array.
    
        Examples
        --------
        >>> a = np.array([[[1,0,1],
        ...                [0,1,0]],
        ...               [[1,1,0],
        ...                [0,0,1]]])
        >>> b = np.packbits(a, axis=-1)
        >>> b
        array([[[160],[64]],[[192],[32]]], dtype=uint8)
    
        Note that in binary 160 = 1010 0000, 64 = 0100 0000, 192 = 1100 0000,
        and 32 = 0010 0000.
    """
    pass

def ravel_multi_index(multi_index, dims, mode='raise', order='C'): # real signature unknown; restored from __doc__
    """
    ravel_multi_index(multi_index, dims, mode='raise', order='C')
    
        Converts a tuple of index arrays into an array of flat
        indices, applying boundary modes to the multi-index.
    
        Parameters
        ----------
        multi_index : tuple of array_like
            A tuple of integer arrays, one array for each dimension.
        dims : tuple of ints
            The shape of array into which the indices from ``multi_index`` apply.
        mode : {'raise', 'wrap', 'clip'}, optional
            Specifies how out-of-bounds indices are handled.  Can specify
            either one mode or a tuple of modes, one mode per index.
    
            * 'raise' -- raise an error (default)
            * 'wrap' -- wrap around
            * 'clip' -- clip to the range
    
            In 'clip' mode, a negative index which would normally
            wrap will clip to 0 instead.
        order : {'C', 'F'}, optional
            Determines whether the multi-index should be viewed as indexing in
            C (row-major) order or FORTRAN (column-major) order.
    
        Returns
        -------
        raveled_indices : ndarray
            An array of indices into the flattened version of an array
            of dimensions ``dims``.
    
        See Also
        --------
        unravel_index
    
        Notes
        -----
        .. versionadded:: 1.6.0
    
        Examples
        --------
        >>> arr = np.array([[3,6,6],[4,5,1]])
        >>> np.ravel_multi_index(arr, (7,6))
        array([22, 41, 37])
        >>> np.ravel_multi_index(arr, (7,6), order='F')
        array([31, 41, 13])
        >>> np.ravel_multi_index(arr, (4,6), mode='clip')
        array([22, 23, 19])
        >>> np.ravel_multi_index(arr, (4,4), mode=('clip','wrap'))
        array([12, 13, 13])
    
        >>> np.ravel_multi_index((3,1,4,1), (6,7,8,9))
        1621
    """
    pass

def unpackbits(myarray, axis=None): # real signature unknown; restored from __doc__
    """
    unpackbits(myarray, axis=None)
    
        Unpacks elements of a uint8 array into a binary-valued output array.
    
        Each element of `myarray` represents a bit-field that should be unpacked
        into a binary-valued output array. The shape of the output array is either
        1-D (if `axis` is None) or the same shape as the input array with unpacking
        done along the axis specified.
    
        Parameters
        ----------
        myarray : ndarray, uint8 type
           Input array.
        axis : int, optional
           Unpacks along this axis.
    
        Returns
        -------
        unpacked : ndarray, uint8 type
           The elements are binary-valued (0 or 1).
    
        See Also
        --------
        packbits : Packs the elements of a binary-valued array into bits in a uint8
                   array.
    
        Examples
        --------
        >>> a = np.array([[2], [7], [23]], dtype=np.uint8)
        >>> a
        array([[ 2],
               [ 7],
               [23]], dtype=uint8)
        >>> b = np.unpackbits(a, axis=1)
        >>> b
        array([[0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1, 1, 1],
               [0, 0, 0, 1, 0, 1, 1, 1]], dtype=uint8)
    """
    pass

def unravel_index(indices, dims, order='C'): # real signature unknown; restored from __doc__
    """
    unravel_index(indices, dims, order='C')
    
        Converts a flat index or array of flat indices into a tuple
        of coordinate arrays.
    
        Parameters
        ----------
        indices : array_like
            An integer array whose elements are indices into the flattened
            version of an array of dimensions ``dims``. Before version 1.6.0,
            this function accepted just one index value.
        dims : tuple of ints
            The shape of the array to use for unraveling ``indices``.
        order : {'C', 'F'}, optional
            .. versionadded:: 1.6.0
    
            Determines whether the indices should be viewed as indexing in
            C (row-major) order or FORTRAN (column-major) order.
    
        Returns
        -------
        unraveled_coords : tuple of ndarray
            Each array in the tuple has the same shape as the ``indices``
            array.
    
        See Also
        --------
        ravel_multi_index
    
        Examples
        --------
        >>> np.unravel_index([22, 41, 37], (7,6))
        (array([3, 6, 6]), array([4, 5, 1]))
        >>> np.unravel_index([31, 41, 13], (7,6), order='F')
        (array([3, 6, 6]), array([4, 5, 1]))
    
        >>> np.unravel_index(1621, (6,7,8,9))
        (3, 1, 4, 1)
    """
    pass

def _insert(*args, **kwargs): # real signature unknown
    """ Insert vals sequentially into equivalent 1-d positions indicated by mask. """
    pass

# no classes
