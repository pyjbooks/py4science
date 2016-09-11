import pickle  # 標準ライブラリpickleの読み込み

# 保存するオブジェクトの準備
mydata = [1, 2, 3]

# オブジェクト（mydata）をファイル'pickle1.pickle'（拡張子は.pickleでなくても良い）に保存
with open('pickle1.pickle', 'wb') as f:
    pickle.dump(mydata, f)

# ファイル'pickle1.pickle'からデータを取り出してdatに代入
with open('pickle1.pickle', 'rb') as f:
    dat = pickle.load(f)
