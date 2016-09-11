# クラスの定義
class MyClass(object):  # (1)継承するクラスなし
    """ (2)簡単なクラスの例のDocstring """
    # (3)クラスのデータx、yの定義
    x = 0
    y = 0

    def my_print(self):
        self.x += 1  # xをインスタンス固有のオブジェクトとして扱う
        MyClass.y += 1  # yをクラス固有のオブジェクトとして扱う
        print('(x, y) = ({}, {})'.format(self.x, self.y))


# クラスのインスタンス化
f = MyClass  # (5)()が付いてない場合はクラスに別名を付けただけ
a = MyClass()  # (6)MyClassクラスのインスタンスを生成しaという名前を付ける
b = f()  # (7)f()はMyClass()と同じ意味（別名を使っている。(5)参照）
# (8)メソッドの実行
a.my_print()
b.my_print()
b.my_print()
