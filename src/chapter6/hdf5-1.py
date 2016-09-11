import h5py
import numpy as np

# 保存するデータを生成
t = np.arange(0, 5, 0.1)
y = np.sin(2*np.pi*0.3*t)
dist = [2, 5, 1, 3, 8, 9, 12]

# データの一部を階層構造にして保存
with h5py.File('data1.h5', 'w') as f:
    f.create_group('wave')
    f.create_dataset('wave/t', data=t)
    f.create_dataset('wave/y', data=y)
    f.create_dataset('dist', data=dist)

# withブロックを抜けると f は一旦閉じられる

# データの読み出し
with h5py.File('data1.h5', 'r') as f:
    t = np.array(f['wave/t'])  # 以下、ndarrayとして読み出し
    y = np.array(f['wave/y'])
    dist = np.array(f['dist'])
