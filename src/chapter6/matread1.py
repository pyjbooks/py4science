import numpy as np
import scipy as sp

# 保存するデータを生成
t = np.arange(0, 5, 0.1)
y = np.sin(2*np.pi*0.3*t)

# MAT-fileの書き出し例
out_dat = {}
out_dat['time'] = t  # ndarrayのtをtimeという名前で格納
out_dat['y'] = y
sp.io.savemat('data2.mat', out_dat, format='5')

# MAT-fileの読み込み例
matdat = sp.io.loadmat('data1.mat', squeeze_me=True)
tt = matdat['time']  # ndarray が生成される
