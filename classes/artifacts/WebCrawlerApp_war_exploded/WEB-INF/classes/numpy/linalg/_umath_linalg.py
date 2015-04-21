# encoding: utf-8
# module numpy.linalg._umath_linalg
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/linalg/_umath_linalg.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

__version__ = '0.1.4'

# functions

def add3(x1, x2, x3, out=None): # real signature unknown; restored from __doc__
    """
    add3(x1, x2, x3[, out])
    
    3-way element-wise addition. a,b,c -> a+b+c for all elements.
    """
    pass

def cholesky_lo(x, out=None): # real signature unknown; restored from __doc__
    """
    cholesky_lo(x[, out])
    
    cholesky decomposition of hermitian positive-definite matrices. 
    Broadcast to all outer dimensions. 
        "(m,m)->(m,m)"
    """
    pass

def cholesky_up(x, out=None): # real signature unknown; restored from __doc__
    """
    cholesky_up(x[, out])
    
    cholesky decomposition of hermitian positive-definite matrices. 
    Broadcast to all outer dimensions. 
        "(m,m)->(m,m)"
    """
    pass

def chosolve1_lo(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    chosolve1_lo(x1, x2[, out])
    
    solve a system using cholesky decomposition.
    """
    pass

def chosolve1_up(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    chosolve1_up(x1, x2[, out])
    
    solve a system using cholesky decomposition.
    """
    pass

def chosolve_lo(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    chosolve_lo(x1, x2[, out])
    
    solve for symmetric/hermitian matrices using cholesky factorization.
    """
    pass

def chosolve_up(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    chosolve_up(x1, x2[, out])
    
    solve for symmetric/hermitian matrices using cholesky factorization.
    """
    pass

def det(x, out=None): # real signature unknown; restored from __doc__
    """
    det(x[, out])
    
    det of the last two dimensions and broadcast on the rest. 
        "(m,m)->()"
    """
    pass

def dotc1d(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    dotc1d(x1, x2[, out])
    
    inner on the last dimension and broadcast on the rest 
        "(i),(i)->()"
    """
    pass

def eig(x, out1=None, out2=None): # real signature unknown; restored from __doc__
    """
    eig(x[, out1, out2])
    
    eig on the last two dimension and broadcast to the rest. 
    Results in a vector with the  eigenvalues and a matrix with the eigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigh_lo(x, out1=None, out2=None): # real signature unknown; restored from __doc__
    """
    eigh_lo(x[, out1, out2])
    
    eigh on the last two dimension and broadcast to the rest, using lower triangle 
    Results in a vector of eigenvalues and a matrix with theeigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigh_up(x, out1=None, out2=None): # real signature unknown; restored from __doc__
    """
    eigh_up(x[, out1, out2])
    
    eigh on the last two dimension and broadcast to the rest, using upper triangle. 
    Results in a vector of eigenvalues and a matrix with the eigenvectors. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigvals(x, out=None): # real signature unknown; restored from __doc__
    """
    eigvals(x[, out])
    
    eigvals on the last two dimension and broadcast to the rest. 
    Results in a vector of eigenvalues. 
        "(m,m)->(m),(m,m)"
    """
    pass

def eigvalsh_lo(x, out=None): # real signature unknown; restored from __doc__
    """
    eigvalsh_lo(x[, out])
    
    eigh on the last two dimension and broadcast to the rest, using lower triangle. 
    Results in a vector of eigenvalues and a matrix with theeigenvectors. 
        "(m,m)->(m)"
    """
    pass

def eigvalsh_up(x, out=None): # real signature unknown; restored from __doc__
    """
    eigvalsh_up(x[, out])
    
    eigvalsh on the last two dimension and broadcast to the rest, using upper triangle. 
    Results in a vector of eigenvalues and a matrix with theeigenvectors.
        "(m,m)->(m)"
    """
    pass

def inner1d(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    inner1d(x1, x2[, out])
    
    inner on the last dimension and broadcast on the rest 
        "(i),(i)->()"
    """
    pass

def innerwt(x1, x2, x3, out=None): # real signature unknown; restored from __doc__
    """
    innerwt(x1, x2, x3[, out])
    
    inner on the last dimension using 3 operands and broadcast on the rest 
        "(i),(i),(i)->()"
    """
    pass

def inv(x, out=None): # real signature unknown; restored from __doc__
    """
    inv(x[, out])
    
    compute the inverse of the last two dimensions and broadcast to the rest. 
    Results in the inverse matrices. 
        "(m,m)->(m,m)"
    """
    pass

def matrix_multiply(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    matrix_multiply(x1, x2[, out])
    
    dot on the last two dimensions and broadcast on the rest 
        "(m,k),(k,n)->(m,n)"
    """
    pass

def multiply3(x1, x2, x3, out=None): # real signature unknown; restored from __doc__
    """
    multiply3(x1, x2, x3[, out])
    
    3-way element-wise product. a,b,c -> a*b*c for all elements.
    """
    pass

def multiply3_add(x1, x2, x3, x4, out=None): # real signature unknown; restored from __doc__
    """
    multiply3_add(x1, x2, x3, x4[, out])
    
    3-way element-wise product plus addition. a,b,c,d -> a*b*c+d for all elements.
    """
    pass

def multiply4(x1, x2, x3, x4, out=None): # real signature unknown; restored from __doc__
    """
    multiply4(x1, x2, x3, x4[, out])
    
    4-way element-wise product. a,b,c,d -> a*b*c*d for all elements.
    """
    pass

def multiply4_add(x1, x2, x3, x4, x5, out=None): # real signature unknown; restored from __doc__
    """
    multiply4_add(x1, x2, x3, x4, x5[, out])
    
    4-way element-wise product and addition. a,b,c,d,e -> a*b*c*d+e.
    """
    pass

def multiply_add(x1, x2, x3, out=None): # real signature unknown; restored from __doc__
    """
    multiply_add(x1, x2, x3[, out])
    
    element-wise multiply-add. a,b,c -> a*b+c for all elements.
    """
    pass

def multiply_add2(x1, x2, x3, x4, out=None): # real signature unknown; restored from __doc__
    """
    multiply_add2(x1, x2, x3, x4[, out])
    
    element-wise product with 2 additions. a,b,c,d -> a*b+c+d for all elements.
    """
    pass

def poinv_lo(x, out=None): # real signature unknown; restored from __doc__
    """
    poinv_lo(x[, out])
    
    inverse using cholesky decomposition for symmetric/hermitian matrices.
    """
    pass

def poinv_up(x, out=None): # real signature unknown; restored from __doc__
    """
    poinv_up(x[, out])
    
    inverse using cholesky decomposition for symmetric/hermitian matrices.
    """
    pass

def quadratic_form(x1, x2, x3, out=None): # real signature unknown; restored from __doc__
    """
    quadratic_form(x1, x2, x3[, out])
    
    computes the quadratic form uQv in the inner dimensions, broadcastto the rest 
    Results in the result of uQv for each element of the broadcasteddimensions. 
        "(m),(m,n),(n)->()
    """
    pass

def slogdet(x, out1=None, out2=None): # real signature unknown; restored from __doc__
    """
    slogdet(x[, out1, out2])
    
    slogdet on the last two dimensions and broadcast on the rest. 
    Results in two arrays, one with sign and the other with log of the determinants. 
        "(m,m)->(),()"
    """
    pass

def solve(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    solve(x1, x2[, out])
    
    solve the system a x = b, on the last two dimensions, broadcast to the rest. 
    Results in a matrices with the solutions. 
        "(m,m),(m,n)->(m,n)"
    """
    pass

def solve1(x1, x2, out=None): # real signature unknown; restored from __doc__
    """
    solve1(x1, x2[, out])
    
    solve the system a x = b, for b being a vector, broadcast in the outer dimensions. 
    Results in vectors with the solutions. 
        "(m,m),(m)->(m)"
    """
    pass

def svd_m(x, out=None): # real signature unknown; restored from __doc__
    """
    svd_m(x[, out])
    
    svd when n>=m.
    """
    pass

def svd_m_f(x, out1=None, out2=None, out3=None): # real signature unknown; restored from __doc__
    """
    svd_m_f(x[, out1, out2, out3])
    
    svd when m>=n
    """
    pass

def svd_m_s(x, out1=None, out2=None, out3=None): # real signature unknown; restored from __doc__
    """
    svd_m_s(x[, out1, out2, out3])
    
    svd when m>=n
    """
    pass

def svd_n(x, out=None): # real signature unknown; restored from __doc__
    """
    svd_n(x[, out])
    
    svd when n<=m
    """
    pass

def svd_n_f(x, out1=None, out2=None, out3=None): # real signature unknown; restored from __doc__
    """
    svd_n_f(x[, out1, out2, out3])
    
    svd when m>=n
    """
    pass

def svd_n_s(x, out1=None, out2=None, out3=None): # real signature unknown; restored from __doc__
    """
    svd_n_s(x[, out1, out2, out3])
    
    svd when m>=n
    """
    pass

# no classes
