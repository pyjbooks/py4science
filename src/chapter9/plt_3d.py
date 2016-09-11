from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
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

# データを3次元プロットする
fig = plt.figure(1)  # (1)
ax = fig.add_subplot(111, projection='3d')  # (2)
surf = ax.plot_surface(X, Y, z, cmap=cm.gray)
ax.set_zlim3d(-3.01, 3.01)
plt.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
