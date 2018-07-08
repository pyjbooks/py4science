# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.stats import multivariate_normal

# Matplotlibのプロットのオプション設定
mpl.rcParams['axes.grid'] = True
mpl.rcParams['grid.linestyle'] = "--"
mpl.rcParams['grid.color'] = "black"

# 2次元メッシュを作成
#   元のサンプルコードの「X, Y = np.meshgrid(x, y)」と同じ処理を以下で行う
Y, X = np.mgrid[-2.0:2.0:200j, -3.0:3.0:200j]

# 2変量正規分布で2次元分布データを作成
mvn_1 = multivariate_normal([0.0, 0.0], [[1.0, 0.0], [0.0, 1.0]])
mvn_2 = multivariate_normal([1.0, 1.0], [[1.5**2, 0.0], [0.0, 0.5**2]])
pos = np.dstack((X, Y))
z = 15 * (mvn_1.pdf(pos) - mvn_2.pdf(pos))  # pdf() ： 確率密度関数を呼び出すメソッド

# --- プロットを作成
plt.figure(1)
plt.clf()
# ❶zの値を濃淡の画像として表示
im = plt.imshow(z, interpolation='bilinear', origin='lower',
                cmap=cm.gray, extent=(-3, 3, -2, 2))
# ❷等高線を表示
levels = np.arange(-2.5, 2.5, 0.5)
ctr = plt.contour(z, levels, colors='k', origin='lower',
                  linewidths=2, extent=(-3, 3, -2, 2))
# ❸等高線にラベルをインライン表示
plt.clabel(ctr, levels, inline=1, colors='black', fmt='%1.1f', fontsize=14)
plt.show()
