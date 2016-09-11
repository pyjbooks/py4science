x = 10


class MyClass(object):
    x = 3  # xが所属する名前空間は生成される

    def __init__(self, y):
        self.x += y

    def my_add(self, z):
        x = x + z  # エラー： xのスコープは生成されていない
        # self.x とすれば参照可能


if __name__ == '__main__':
a = MyClass(10)
a.my_add(10)
print(a.x)
