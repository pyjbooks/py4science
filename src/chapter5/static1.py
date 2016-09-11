class MyCalc(object):
    @staticmethod
    def my_add(x, y):
        return x + y

a = MyCalc.my_add(5, 9)  # a = 14 となる（MyCalcのインスタンスを作成しなくてよい）
