def list_by_for(x, y):
    z = []
    append = z.append
    for k in range(len(x)):
        append(x[k]*y[k] + 0.1*y[k])
    return z

def list_by_lc(x, y):
    return [a*b + 0.1*b for a, b in zip(x, y)]

if __name__ == '__main__':
    N1 = 1000000
    x = list(range(N1, 0, -1))
    y = list(range(N1))
    z1 = list_by_for(x, y)  # 実際はこの処理の時間を計測する
    z2 = list_by_lc(x, y)  # 実際はこの処理の時間を計測する
