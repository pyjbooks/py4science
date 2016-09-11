import numpy as np
import time


def mult_basic(N, M, L, a, x, y):
    """ 行列計算は使わずにForループで計算する関数
        ただし、所望のサイズの非ndarrayを作成するのが困難なので、
        入力の変数はNumPyのndarrayとして生成して渡す """
    r = np.empty((N, L))
    for i in range(N):
        for j in range(L):
            tmp = 0.0
            for k in range(M):
                tmp = tmp + a[k]*x[i][k]*y[k][j]
            r[i][j] = tmp
    return r


def mult_fast(N, M, L, a, x, y):
    """ NumPyの関数を使って高速に計算する関数
        関数mult_basicと全く同じ結果を得る"""
    return np.dot(x*a, y)  # 処理の記述はたったの1行


if __name__ == '__main__':
    # 計算に使う配列の生成
    np.random.seed(0)
    N = 10000
    M = 1000
    L = 10000
    a = np.random.random(M) - 0.5
    x = np.random.random((N, M)) - 0.5
    y = np.random.random((M, L)) - 0.5

    # 行列計算は使わずにForループで計算
    ts = time.time()
    r1 = mult_basic(N, M, L, a, x, y)
    te = time.time()
    print("Basic method : %.3f [ms]" % (1000*(te - ts)))

    # NumPyの関数を使って高速に処理
    ts = time.time()
    r2 = mult_fast(N, M, L, a, x, y)
    te = time.time()
    print("Fast method  : %.3f [ms]" % (1000*(te - ts)))
