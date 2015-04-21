# encoding: utf-8
# module scipy.signal._spectral
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/signal/_spectral.so
# by generator 1.136
""" Tools for spectral analysis of unequally sampled signals. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import numpy as np # /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/__init__.pyc

# functions

def lombscargle(x, y, freqs): # real signature unknown; restored from __doc__
    """
    lombscargle(x, y, freqs)
    
        Computes the Lomb-Scargle periodogram.
        
        The Lomb-Scargle periodogram was developed by Lomb [1]_ and further
        extended by Scargle [2]_ to find, and test the significance of weak
        periodic signals with uneven temporal sampling.
    
        The computed periodogram is unnormalized, it takes the value
        ``(A**2) * N/4`` for a harmonic signal with amplitude A for sufficiently
        large N.
    
        Parameters
        ----------
        x : array_like
            Sample times.
        y : array_like
            Measurement values.
        freqs : array_like
            Angular frequencies for output periodogram.
    
        Returns
        -------
        pgram : array_like
            Lomb-Scargle periodogram.
    
        Raises
        ------
        ValueError
            If the input arrays `x` and `y` do not have the same shape.
    
        Notes
        -----
        This subroutine calculates the periodogram using a slightly
        modified algorithm due to Townsend [3]_ which allows the
        periodogram to be calculated using only a single pass through
        the input arrays for each frequency.
    
        The algorithm running time scales roughly as O(x * freqs) or O(N^2)
        for a large number of samples and frequencies.
    
        References
        ----------
        .. [1] N.R. Lomb "Least-squares frequency analysis of unequally spaced
               data", Astrophysics and Space Science, vol 39, pp. 447-462, 1976
    
        .. [2] J.D. Scargle "Studies in astronomical time series analysis. II - 
               Statistical aspects of spectral analysis of unevenly spaced data",
               The Astrophysical Journal, vol 263, pp. 835-853, 1982
    
        .. [3] R.H.D. Townsend, "Fast calculation of the Lomb-Scargle
               periodogram using graphics processing units.", The Astrophysical
               Journal Supplement Series, vol 191, pp. 247-253, 2010
    
        Examples
        --------
        >>> import scipy.signal
    
        First define some input parameters for the signal:
    
        >>> A = 2.
        >>> w = 1.
        >>> phi = 0.5 * np.pi
        >>> nin = 1000
        >>> nout = 100000
        >>> frac_points = 0.9 # Fraction of points to select
         
        Randomly select a fraction of an array with timesteps:
    
        >>> r = np.random.rand(nin)
        >>> x = np.linspace(0.01, 10*np.pi, nin)
        >>> x = x[r >= frac_points]
        >>> normval = x.shape[0] # For normalization of the periodogram
         
        Plot a sine wave for the selected times:
    
        >>> y = A * np.sin(w*x+phi)
    
        Define the array of frequencies for which to compute the periodogram:
        
        >>> f = np.linspace(0.01, 10, nout)
         
        Calculate Lomb-Scargle periodogram:
    
        >>> pgram = sp.signal.lombscargle(x, y, f)
    
        Now make a plot of the input data:
    
        >>> plt.subplot(2, 1, 1)
        <matplotlib.axes.AxesSubplot object at 0x102154f50>
        >>> plt.plot(x, y, 'b+')
        [<matplotlib.lines.Line2D object at 0x102154a10>]
    
        Then plot the normalized periodogram:
    
        >>> plt.subplot(2, 1, 2)
        <matplotlib.axes.AxesSubplot object at 0x104b0a990>
        >>> plt.plot(f, np.sqrt(4*(pgram/normval)))
        [<matplotlib.lines.Line2D object at 0x104b2f910>]
        >>> plt.show()
    """
    pass

# no classes
# variables with complex values

__all__ = [
    'lombscargle',
]

__test__ = {
    u'lombscargle (line 19)': u'\n    lombscargle(x, y, freqs)\n\n    Computes the Lomb-Scargle periodogram.\n    \n    The Lomb-Scargle periodogram was developed by Lomb [1]_ and further\n    extended by Scargle [2]_ to find, and test the significance of weak\n    periodic signals with uneven temporal sampling.\n\n    The computed periodogram is unnormalized, it takes the value\n    ``(A**2) * N/4`` for a harmonic signal with amplitude A for sufficiently\n    large N.\n\n    Parameters\n    ----------\n    x : array_like\n        Sample times.\n    y : array_like\n        Measurement values.\n    freqs : array_like\n        Angular frequencies for output periodogram.\n\n    Returns\n    -------\n    pgram : array_like\n        Lomb-Scargle periodogram.\n\n    Raises\n    ------\n    ValueError\n        If the input arrays `x` and `y` do not have the same shape.\n\n    Notes\n    -----\n    This subroutine calculates the periodogram using a slightly\n    modified algorithm due to Townsend [3]_ which allows the\n    periodogram to be calculated using only a single pass through\n    the input arrays for each frequency.\n\n    The algorithm running time scales roughly as O(x * freqs) or O(N^2)\n    for a large number of samples and frequencies.\n\n    References\n    ----------\n    .. [1] N.R. Lomb "Least-squares frequency analysis of unequally spaced\n           data", Astrophysics and Space Science, vol 39, pp. 447-462, 1976\n\n    .. [2] J.D. Scargle "Studies in astronomical time series analysis. II - \n           Statistical aspects of spectral analysis of unevenly spaced data",\n           The Astrophysical Journal, vol 263, pp. 835-853, 1982\n\n    .. [3] R.H.D. Townsend, "Fast calculation of the Lomb-Scargle\n           periodogram using graphics processing units.", The Astrophysical\n           Journal Supplement Series, vol 191, pp. 247-253, 2010\n\n    Examples\n    --------\n    >>> import scipy.signal\n\n    First define some input parameters for the signal:\n\n    >>> A = 2.\n    >>> w = 1.\n    >>> phi = 0.5 * np.pi\n    >>> nin = 1000\n    >>> nout = 100000\n    >>> frac_points = 0.9 # Fraction of points to select\n     \n    Randomly select a fraction of an array with timesteps:\n\n    >>> r = np.random.rand(nin)\n    >>> x = np.linspace(0.01, 10*np.pi, nin)\n    >>> x = x[r >= frac_points]\n    >>> normval = x.shape[0] # For normalization of the periodogram\n     \n    Plot a sine wave for the selected times:\n\n    >>> y = A * np.sin(w*x+phi)\n\n    Define the array of frequencies for which to compute the periodogram:\n    \n    >>> f = np.linspace(0.01, 10, nout)\n     \n    Calculate Lomb-Scargle periodogram:\n\n    >>> pgram = sp.signal.lombscargle(x, y, f)\n\n    Now make a plot of the input data:\n\n    >>> plt.subplot(2, 1, 1)\n    <matplotlib.axes.AxesSubplot object at 0x102154f50>\n    >>> plt.plot(x, y, \'b+\')\n    [<matplotlib.lines.Line2D object at 0x102154a10>]\n\n    Then plot the normalized periodogram:\n\n    >>> plt.subplot(2, 1, 2)\n    <matplotlib.axes.AxesSubplot object at 0x104b0a990>\n    >>> plt.plot(f, np.sqrt(4*(pgram/normval)))\n    [<matplotlib.lines.Line2D object at 0x104b2f910>]\n    >>> plt.show()\n    \n    ',
}

