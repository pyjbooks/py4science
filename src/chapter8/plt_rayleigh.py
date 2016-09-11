import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# (1)統計分布関数の設定（Freezeしておく）
rv = sp.stats.rayleigh(loc=1)

# (2)上記統計分布関数によるランダム変数の生成
r = rv.rvs(size=3000)

# (3)確率密度関数プロット用のパーセント点データ列
x = np.linspace(rv.ppf(0.01), rv.ppf(0.99), 100)

# 元の確率密度関数と一緒にサンプルしたデータの分布をプロットする
plt.figure(1)
plt.clf()
plt.plot(x, rv.pdf(x), 'k-', lw=2, label='確率密度関数')
plt.hist(r, normed=True, histtype='barstacked', alpha=0.5)
plt.xlabel('値')
plt.ylabel('分布度')
plt.show()
