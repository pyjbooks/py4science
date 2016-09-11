import cProfile
import numpy as np
import pstats


def is_prime(a):
    """ 素数判定プログラム（フェルマーの小定理） """
    a = abs(a)
    if a == 2:
        return True
    if a < 2 or a & 1 == 0:
        return False
    return pow(2, a-1, a) == 1


def mysum(n):
    """ 1からNまでの整数の和を計算する """
    return np.arange(1, n+1).sum()


def task1(n):
    """ 次の２つの処理を行う
       (1) 1からNまでの整数の中から素数を探す
       (2) 1からNまでの整数の和を計算する
    """
    # (1)
    out = []
    append = out.append
    for k in range(1, n+1):
        if is_prime(k):
            append(k)
    # (2)
    a = mysum(n)
    return [out, a]


def task2(n):
    """ 1からNまでのsqrt()を計算する """
    return np.sqrt(np.arange(1, n+1))


def main():
    task1(100000)  # 重い処理
    task2(100000)  # 軽い処理


if __name__ == '__main__':  # (3)
    cProfile.run('main()', filename='main.prof')
    sts = pstats.Stats('main.prof')
    sts.strip_dirs().sort_stats('cumulative').print_stats()
