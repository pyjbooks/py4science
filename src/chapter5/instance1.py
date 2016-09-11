import time


class MyTime(object):
    def __init__(self, hour, minutes, sec):
        self.hour = hour
        self.minutes = minutes
        self.sec = sec

    @staticmethod  # now()をスタティックメソッド化
    def now():
        t = time.localtime()
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

    @staticmethod  # two_hours_later()をスタティックメソッド化
    def two_hours_later():
        t = time.localtime(time.time() + 7200)
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

# クラスMyTimesのインスタンス化を3つの方法で行う
a = MyTime(15, 20, 58)  # __init__を使う通常のインスタンス化
b = MyTime.now()  # スタティックメソッドによるインスタンス化(1)
c = MyTime.two_hours_later()  # スタティックメソッドによるインスタンス化(2)
