# encoding: utf-8
# module scipy.stats._rank
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/stats/_rank.so
# by generator 1.136
"""
Some functions related to ranking data, implemented in Cython for speed.
This file uses fused types, so Cython version 0.16 or later is required.

This module provides the following functions:
    rankdata
        Ranks the data, dealing with ties appropriately.
    tiecorrect
        Tie correction factor for the Mann-Whitney U test (stats.mannwhitnyu)
        and the Kruskal-Wallis H test (stats.kruskal).
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as _np # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.pyc

# functions

def rankdata(a, method='average'): # real signature unknown; restored from __doc__
    """
    rankdata(a, method='average')
    
        Assign ranks to data, dealing with ties appropriately.
    
        Ranks begin at 1.  The `method` argument controls how ranks are assigned
        to equal values.  See [1]_ for further discussion of ranking methods.
    
        Parameters
        ----------
        a : array_like
            The array of values to be ranked.  The array is first flattened.
        method : str, optional
            The method used to assign ranks to tied elements.
            The options are 'average', 'min', 'max', 'dense' and 'ordinal'.
    
            'average':
                The average of the ranks that would have been assigned to
                all the tied values is assigned to each value.
            'min':
                The minimum of the ranks that would have been assigned to all
                the tied values is assigned to each value.  (This is also
                referred to as "competition" ranking.)
            'max':
                The maximum of the ranks that would have been assigned to all
                the tied values is assigned to each value.
            'dense':
                Like 'min', but the rank of the next highest element is assigned
                the rank immediately after those assigned to the tied elements.
            'ordinal':
                All values are given a distinct rank, corresponding to the order
                that the values occur in `a`.
    
            The default is 'average'.
    
        Returns
        -------
        ranks : ndarray
             An array of length equal to the size of `a`, containing rank
             scores.
    
        Notes
        -----
        All floating point types are converted to numpy.float64 before ranking.
        This may result in spurious ties if an input array of floats has a wider
        data type than numpy.float64 (e.g. numpy.float128).
    
        References
        ----------
        .. [1] "Ranking", http://en.wikipedia.org/wiki/Ranking
    
        Examples
        --------
        >>> rankdata([0, 2, 3, 2])
        array([ 1. ,  2.5,  4. ,  2.5])
        >>> rankdata([0, 2, 3, 2], method='min')
        array([ 1.,  2.,  4.,  2.])
        >>> rankdata([0, 2, 3, 2], method='max')
        array([ 1.,  3.,  4.,  3.])
        >>> rankdata([0, 2, 3, 2], method='dense')
        array([ 1.,  2.,  3.,  2.])
        >>> rankdata([0, 2, 3, 2], method='ordinal')
        array([ 1.,  2.,  4.,  3.])
    """
    pass

def tiecorrect(rankvals): # real signature unknown; restored from __doc__
    """
    tiecorrect(rankvals)
    
        Tie correction factor for ties in the Mann-Whitney U and
        Kruskal-Wallis H tests.
    
        Parameters
        ----------
        rankvals : array_like
            A 1-D sequence of ranks.  Typically this will be the array
            returned by `stats.rankdata`.
    
        Returns
        -------
        factor : float
            Correction factor for U or H.
    
        See Also
        --------
        rankdata : Assign ranks to the data
        mannwhitneyu : Mann-Whitney rank test
        kruskal : Kruskal-Wallis H test
    
        References
        ----------
        .. [1] Siegel, S. (1956) Nonparametric Statistics for the Behavioral
               Sciences.  New York: McGraw-Hill.
    
        Examples
        --------
        >>> tiecorrect([1, 2.5, 2.5, 4])
        0.9
        >>> ranks = rankdata([1, 3, 2, 4, 5, 7, 2, 8, 4])
        >>> ranks
        array([ 1. ,  4. ,  2.5,  5.5,  7. ,  8. ,  2.5,  9. ,  5.5])
        >>> tiecorrect(ranks)
        0.9833333333333333
    """
    pass

# no classes
# variables with complex values

_tie_method_map = {
    'average': 0,
    'dense': 3,
    'max': 2,
    'min': 1,
    'ordinal': 4,
}

__test__ = {
    u'rankdata (line 92)': u'\n    rankdata(a, method=\'average\')\n\n    Assign ranks to data, dealing with ties appropriately.\n\n    Ranks begin at 1.  The `method` argument controls how ranks are assigned\n    to equal values.  See [1]_ for further discussion of ranking methods.\n\n    Parameters\n    ----------\n    a : array_like\n        The array of values to be ranked.  The array is first flattened.\n    method : str, optional\n        The method used to assign ranks to tied elements.\n        The options are \'average\', \'min\', \'max\', \'dense\' and \'ordinal\'.\n\n        \'average\':\n            The average of the ranks that would have been assigned to\n            all the tied values is assigned to each value.\n        \'min\':\n            The minimum of the ranks that would have been assigned to all\n            the tied values is assigned to each value.  (This is also\n            referred to as "competition" ranking.)\n        \'max\':\n            The maximum of the ranks that would have been assigned to all\n            the tied values is assigned to each value.\n        \'dense\':\n            Like \'min\', but the rank of the next highest element is assigned\n            the rank immediately after those assigned to the tied elements.\n        \'ordinal\':\n            All values are given a distinct rank, corresponding to the order\n            that the values occur in `a`.\n\n        The default is \'average\'.\n\n    Returns\n    -------\n    ranks : ndarray\n         An array of length equal to the size of `a`, containing rank\n         scores.\n\n    Notes\n    -----\n    All floating point types are converted to numpy.float64 before ranking.\n    This may result in spurious ties if an input array of floats has a wider\n    data type than numpy.float64 (e.g. numpy.float128).\n\n    References\n    ----------\n    .. [1] "Ranking", http://en.wikipedia.org/wiki/Ranking\n\n    Examples\n    --------\n    >>> rankdata([0, 2, 3, 2])\n    array([ 1. ,  2.5,  4. ,  2.5])\n    >>> rankdata([0, 2, 3, 2], method=\'min\')\n    array([ 1.,  2.,  4.,  2.])\n    >>> rankdata([0, 2, 3, 2], method=\'max\')\n    array([ 1.,  3.,  4.,  3.])\n    >>> rankdata([0, 2, 3, 2], method=\'dense\')\n    array([ 1.,  2.,  3.,  2.])\n    >>> rankdata([0, 2, 3, 2], method=\'ordinal\')\n    array([ 1.,  2.,  4.,  3.])\n    ',
    u'tiecorrect (line 192)': u'\n    tiecorrect(rankvals)\n\n    Tie correction factor for ties in the Mann-Whitney U and\n    Kruskal-Wallis H tests.\n\n    Parameters\n    ----------\n    rankvals : array_like\n        A 1-D sequence of ranks.  Typically this will be the array\n        returned by `stats.rankdata`.\n\n    Returns\n    -------\n    factor : float\n        Correction factor for U or H.\n\n    See Also\n    --------\n    rankdata : Assign ranks to the data\n    mannwhitneyu : Mann-Whitney rank test\n    kruskal : Kruskal-Wallis H test\n\n    References\n    ----------\n    .. [1] Siegel, S. (1956) Nonparametric Statistics for the Behavioral\n           Sciences.  New York: McGraw-Hill.\n\n    Examples\n    --------\n    >>> tiecorrect([1, 2.5, 2.5, 4])\n    0.9\n    >>> ranks = rankdata([1, 3, 2, 4, 5, 7, 2, 8, 4])\n    >>> ranks\n    array([ 1. ,  4. ,  2.5,  5.5,  7. ,  8. ,  2.5,  9. ,  5.5])\n    >>> tiecorrect(ranks)\n    0.9833333333333333\n\n    ',
}

