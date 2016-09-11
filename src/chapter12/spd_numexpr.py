import time
import numexpr as ne
import numpy as np

# 大きなNumPyの配列を作る
N = 10000000
a = np.random.randn(N)
b = np.random.randn(N)

# NumPyに三角関数計算と積和演算をさせて時間を計測
ts1 = time.clock()
c1 = (a * np.sin(b)).sum()
te1 = time.clock()
print('NumPy : %.6f [s]' % (te1 - ts1))

# Numexprに上記と同じ計算をさせて時間を計測
ts2 = time.clock()
c2 = ne.evaluate('sum(a * sin(b))')
te2 = time.clock()
print('Numexpr : %.6f [s]' % (te2 - ts2))

# どれくらい高速化できたか評価する
print('%.3f[％] 早く処理できました。' % (100-100*(te2-ts2)/(te1-ts1)))
