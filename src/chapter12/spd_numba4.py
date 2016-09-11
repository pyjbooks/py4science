import numpy as np
from numba import jit

nthreads = 2  # 2コアのCPUで検証するのでスレッド数を2にする
size = 10000000


# これが高速化する前の関数
def func_np(a, b):
    return np.exp(2.1 * a + 3.2 * b)


# Numbaで高速化した関数
@jit('void(double[:], double[:], double[:])', nopython=True, nogil=True)
def inner_func_nb(result, a, b):
    for i in range(len(result)):
        result[i] = np.exp(2.1 * a[i] + 3.2 * b[i])
