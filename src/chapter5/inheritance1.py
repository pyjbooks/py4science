# (1)クラスMyBaseの定義（MyDerivの基底クラス）
class MyBase(object):
    coeff = 2

    def __init__(self, x):
        self.x = x

    def mult(self):
        return self.coeff * self.x


# (2)クラスMyDerivの定義（MyBaseの派生クラス）
class MyDeriv(MyBase):
    coeff = 3  # (3)属性を再定義

    # (4)コンストラクタの再定義
    def __init__(self, x, y):
        super().__init__(x)  # (5)基底クラスのメソッドの呼び出し例
        self.y = y  # (6)属性yを追加しインスタンス化時に初期化

    # (7)新しいメソッドを追加
    def mult2(self):
        return self.coeff * self.x * self.y


# (8)MyBaseとMyDerivを使った計算例
a = MyBase(3)  # MyBaseのインスタンスを生成
print(a.mult())  # 結果は 2*3=6
b = MyDeriv(3, 5)  # MyDerivのインスタンスを生成
print(b.mult())  # 結果は 3*3=9 （継承したメソッドの確認）
print(b.mult2())  # 結果は 3*5*5=45（追加したメソッドの確認）
