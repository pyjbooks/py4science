import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

# (1)-πからπまで0.1刻みの配列をつくる
x = np.arange(-np.pi, np.pi, 0.1)
# 配列xに対してsin(x)を計算（sin()はユニバーサル関数）
y1 = sin(x)
# 配列xに対してcos(x)を計算
y2 = cos(x)
plt.figure(1)
plt.clf()

# x、yを描画
plt.plot(x, y1, label='正弦関数')
plt.plot(x, y2, 'r*', markersize=10, label='余弦関数')  # (2)
# 軸ラベル設定
plt.xlabel('X軸')
plt.ylabel('Y軸')
# 凡例の描画
plt.legend(loc='best')
# (3)描画
plt.show()
