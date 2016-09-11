import numpy as np

# npyにndarrayを1つ保存
a = np.array([1, 2, 3])
np.save('foo', a)

# npyからndarrayを復元
a2 = np.load('foo.npy')

# npz（複数のndarrayアーカイブ）にndarrayを出力
b = np.array([[1, 2], [3, 4]])
np.savez('foo.npz', a=a, b2=b)  # bにb2という名前を付けて保存

# npzファイルの入力
with np.load('foo.npz') as data:
    a3 = data['a']  # aという名前の変数だけ取り出す
    b3 = data['b2']
