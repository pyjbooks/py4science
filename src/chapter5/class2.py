# クラスの定義
class MyClass(object):  # 継承するクラス無し
    """ 簡単なクラスの例のDocstring """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def my_print(self):
        print('{}年のオリンピック開催地は{}'.format(self.x, self.y))

# クラスのインスタンス化
a = MyClass(2016, 'リオデジャネイロ')
b = MyClass(2020, '東京')
# メソッドの実行
a.my_print()
b.my_print()
