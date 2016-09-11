def my_add(x, y):
    """ 2つの数字を加算する """
    out = x + z  # バグ：zという変数は定義されていない
    return out + y

if __name__ == "__main__":
    a, b = 3, 4
    z = my_add(a, b)
    print(z)
