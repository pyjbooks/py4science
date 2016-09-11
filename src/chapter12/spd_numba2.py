import numpy as np
import time
from numba import jitclass  # import jitclass decorator
from numba import int32, float64  # 型名称をimport

# クラスの属性の型を規定
spec = [
    ('size', int32),
    ('arr', float64[:]),
]


@jitclass(spec)
class RandomCode(object):

    def __init__(self, size):
        self.size = size
        self.arr = np.random.randn(size)

    def bit_code(self):
        for i in range(self.size):
            if self.arr[i] >= 0.5:
                self.arr[i] = 1
            else:
                self.arr[i] = -1
        return self.arr


if __name__ == '__main__':
    a = RandomCode(1000000)
    ts = time.clock()
    cdat = a.bit_code()
    print('コード生成所用時間 : {0:.3f}[s]'.format(time.clock() - ts))
