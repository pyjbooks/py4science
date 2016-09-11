import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import bivariate_normal

# 2次元メッシュを作成
N = 200
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-2.0, 2.0, N)
X, Y = np.meshgrid(x, y)

# 2変量正規分布で2次元分布データを作成
z = 15 * (bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0) -
          bivariate_normal(X, Y, 1.5, 0.5, 1, 1))

# --- プロットを作成
plt.figure(1)

# (1)zの値を濃淡の画像として表示
im = plt.imshow(z, interpolation='bilinear', origin='lower',
                cmap=cm.gray, extent=(-3, 3, -2, 2))

# (2)等高線を表示
levels = np.arange(-3, 2.5, 0.5)
ctr = plt.contour(z, levels, colors='k', origin='lower',
                  linewidths=2, extent=(-3, 3, -2, 2))

# (3)等高線にラベルをインライン表示
plt.clabel(ctr, levels, inline=1, colors='black',
           fmt='%1.1f', fontsize=14)
plt.show()
