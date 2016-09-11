import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
# (1)scipyとは別にimportが必要
from scipy.fftpack import fft

# (2)30 Hzの信号とノイズの合成信号yを生成
Fs = 500  # サンプリング周波数
T = 1/Fs  # サンプリング時間
L = 2**14  # 信号の長さ（サンプリング数）
t = sp.arange(L)*T  # 時間ベクトル
y = np.sin(2*np.pi*30*t) + 5*sp.randn(t.size)  # 信号生成

# (3)FFTを実行
Y = sp.fftpack.fft(y, L)/L
f = (Fs/L)*sp.arange(L/2 + 1)  # 周波数ベクトル取得

# (4)「元の時系列データ」と「FFTによる周波数解析結果」のプロット
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlabel('時間 [s]')
plt.ylabel('値')
plt.subplot(2, 1, 2)
plt.plot(f, 2*abs(Y[:L/2 + 1]))
plt.xlabel('周波数 [Hz]')
plt.ylabel('|Y(f)|')
