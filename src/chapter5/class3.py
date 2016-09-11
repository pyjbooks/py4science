# (1)グローバル名前空間にxを定義
x = 100


class MyClass:
    # (2)このクラスのデータとしてiとxを定義
    i = 10  # メソッドprice()の中で参照される
    x += 2  # グローバル名前空間のxに２を加えてデータxを定義
    xx = x + 2  # (3)MyClassの中のデータのxを参照
    print('xx = ', xx)

    def price(self):
        y = self.i * x  # (4)グローバル名前空間のオブジェクトxを参照
    z = self.i * self.x  # (5)インスタンス属性→クラス属性の順に検索して参照
    # z = i * x  # (6)これはエラー（ここからデータiは見えない）
    print("price y = %d" % y)
    print("price z = %d" % z)

    def shop(self):
        # price()  # (7)エラーとなる（NameError）
        self.price()  # (8)これはOK
        # MyClass.price(self) # (9)これでもOK
        MyClass.i = 20  # (10)クラスのデータを変更
        print("メソッド shop 終了")


# (11)動作確認のための実行コード
if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    a.shop()  # この中で MyClass.i = 20 が実行される
    print('(a.i, b.i) = ({}, {})'.format(a.i, b.i))
    a.i = 2  # インスタンス属性を設定
    MyClass.i = 4  # クラス属性の値を変更
    print('(a.i, b.i) = ({}, {})'.format(a.i, b.i))
