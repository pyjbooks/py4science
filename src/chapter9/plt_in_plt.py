import numpy as np
import matplotlib.pyplot as plt

# サブプロットを2つ並べる
plt.figure(1)
plt.subplot(2, 1, 1)
x = np.arange(-np.pi, np.pi, 0.1)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))

# 図枠の中に図枠を設定
plt.axes([0.55, 0.3, 0.3, 0.4])
plt.text(0.5, 0.5, 'axes([0.55, 0.3, 0.3, 0.4])', ha='center', va='center')
plt.show()
