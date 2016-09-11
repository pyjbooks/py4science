import scipy as sp
import matplotlib.pyplot as plt

# (1)scipyとは別にimportが必要
from scipy import signal

# (2)線形システムの定義
s1 = sp.signal.lti([1], [1, 1])

# (3)bode関数による解析処理
w, mag, phase = sp.signal.bode(s1)

# (4)ボード線図の描画
plt.figure(1)
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  # Bode magnitude plot
plt.box('on')
plt.xlabel('周波数 [rad/s]')
plt.ylabel('ゲイン [dB]')
plt.title('ボード線図')
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)  # Bode phase plot
plt.xlabel('周波数 [rad/s]')
plt.ylabel('位相 [deg]')
plt.box('on')
plt.show()
