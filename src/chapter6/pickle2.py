import pickle
import numpy as np


# 保存ｌするオブジェクトの準備
a = np.float(2.3)
b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
c = {'yokohama': 1, 'tokyo': 2, 'nagoya': 3}

# 複数オブジェクトを1つのファイルにpickle化
with open('pickle1.pickle', 'wb') as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

# pickle化したファイルから複数オブジェクトを読み出す
with open('pickle1.pickle', 'rb') as f:
    a2 = pickle.load(f)
    b2 = pickle.load(f)
    c2 = pickle.load(f)
