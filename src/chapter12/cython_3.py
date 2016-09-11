import cython_2
import numpy as np
import time

N = 10000000


# cython_2.pyの関数のPythonオリジナル
def matrix_cal(X, Y, a):
    for i in range(N):
        if Y[i] < 0:
            Y[i] += 10.0 + 1e-7*i
    return a*X + np.exp(Y)

if __name__ == '__main__':
    # 計算に使うndarrayを生成
    a = 3.4
    X = np.random.randn(N)
    Y = np.random.randn(N)
    # Cython版で計算
    ts = time.clock()
    Z = cython_2.matrix_cal_cy(X, Y, a)
    print('Cython版の処理の時間: {0:.3f}[s]'.format(time.clock() - ts))
    # オリジナルのmatrix_calで計算
    ts = time.clock()
    Z = matrix_cal(X, Y, a)
    print('オリジナル版の処理の時間: {0:.3f}[s]'.format(time.clock() - ts))
