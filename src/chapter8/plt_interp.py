import numpy as np
import matplotlib.pyplot as plt

# (1)名前が長いので別名を付ける
import scipy.interpolate as ipl


# (2)元の関数の定義
def f(x):
    return (x-7) * (x-2) * (x+0.2) * (x-4)

# (3)元データ生成（正解の値）
x = np.linspace(0, 8, 81)
y = np.array(list(map(f, x)))

# (4)補間前の間隔が広いデータ
x0 = np.arange(9)
y0 = np.array(list(map(f, x0)))

# (5)補間関数の設定（線形補間）
#  補間関数の設定（線形補間／3次スプライン）
f_linear = ipl.interp1d(x0, y0, bounds_error=False)
f_cubic = ipl.interp1d(x0, y0, kind='cubic', bounds_error=False)
#  補間処理の実行
y1 = f_linear(x)  # 線形補間
y2 = f_cubic(x)  # 3次スプライン補間

# (6)補間データと元データの比較プロット
plt.figure(1)
plt.clf()
plt.plot(x, y, 'k-', label='元の関数')
plt.plot(x0, y0, 'ko', label='補間前データ', markersize=10)
plt.plot(x, y1, 'k:', label='線形補間', linewidth=4)
plt.plot(x, y2, 'k--', label='3次スプライン補間', linewidth=4, alpha=0.7)
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
