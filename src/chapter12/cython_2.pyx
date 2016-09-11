""" NumPyのndarrayを使う関数のCythonプログラム例 """

cimport numpy as np
from cython.parallel import prange

N = 10000000

def matrix_cal_cy(np.ndarray[double, ndim=1] X,
                  np.ndarray[double, ndim=1] Y, double a):
    cdef int i
    for i in prange(N, nogil=True):
        if Y[i] < 0:
            Y[i] += 10.0 +  1e-7*i
    return (a*X + np.exp(Y))
