import numpy as np  # NumPyをimport
import csv  # 標準モジュールcsvを読み込む


# CSVファイルからの読み込み
dat = np.loadtxt('data1.csv', delimiter=',', skiprows=1, dtype=float)

# ndarrayのdatをCSVファイルへ書き込み（日本語を扱えない点に注意）
np.savetxt('data1_saved.csv', dat, fmt='%.1f,%.8f,%d',
           header='time,vel,alt', comments='')

# ndarrayのdatをCSVファイルの書き込み（日本語も扱える）
with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    f.write('time,速度,高度\n')
    writer = csv.writer(f)
    writer.writerows(dat)
