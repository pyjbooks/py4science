import pickle
import numpy as np


def pickle_vars(fname, mode='wb', **vars):
    """
    使い方
    pickle_vars('作成するファイル名', a=a, b=b, c=c)
    引数には作成するファイル名と、オブジェクトを列挙する
    """
    dic = {}
    for key in vars.keys():
        exec('dic[key]=vars.get(key)')
    with open(fname, mode) as f:
        pickle.dump(dic, f)
    return dic

if __name__ == "__main__":
    # 各種オブジェクトを生成
    a = np.float(2.3)
    b = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
    c = {'yokohama': 1, 'tokyo': 2, 'nagoya': 3}
    # 複数の変数とそのデータを保存
    saved_dat = pickle_vars('pickle1.pickle', a=a, b=b, c=c)
    # pickle化したファイルからデータを読み出す
    with open('pickle1.pickle', 'rb') as f:
        dat = pickle.load(f)
        for key in dat.keys():
            exec(key+'=dat.get(key)')  # 元の変数でデータを復元
