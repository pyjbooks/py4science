""" fc.py """
import numpy as np
n = 20


def func_c():
    a = np.arange(0, n*n).reshape(n, n) + np.identity(n)
    b = np.arange(0, n)
    x = np.dot(np.linalg.inv(a), b)
