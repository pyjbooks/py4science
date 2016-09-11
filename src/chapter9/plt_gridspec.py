import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
import numpy as np

G = gs.GridSpec(3, 3)  # ← (1)

axes_1 = plt.subplot(G[0, :])  # ← (2)
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, '図枠1', ha='center', va='center', size=22)

axes_2 = plt.subplot(G[1, :-1])
x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.text(-0.5, 0, '図枠2', ha='center', va='center', size=22)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, '図枠3', ha='center', va='center', size=22)

axes_4 = plt.subplot(G[-1, 0])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, '図枠4', ha='center', va='center', size=22)

axes_5 = plt.subplot(G[-1, -2])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, '図枠5', ha='center', va='center', size=22)

plt.show()
