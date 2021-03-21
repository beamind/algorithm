# weights表示一堆西瓜的重量，labels表示西瓜是否是好瓜，好瓜用1表示，坏瓜用0表示。如果仅用重量阈值threshold衡量是否是好瓜，找到错误率最低的阈值。


def f(weights, labels):
    n = len(weights)
    data = list(zip(weights, labels))
    data.sort()
    a = [0] * n
    b = [0] * n
    if data[n - 1][1] == 0:
        a[n - 1] = 1
    for i in range(n - 2, -1, -1):
        if data[i][1] == 0:
            a[i] = a[i + 1] + 1
        else:
            a[i] = a[i + 1]
    for i in range(1, n):
        if data[i - 1][1] == 1:
            b[i] = b[i - 1] + 1
        else:
            b[i] = b[i - 1]
    threshold, wrong = -1, float('inf')
    for i in range(n):
        if a[i] + b[i] < wrong:
            wrong = a[i] + b[i]
            threshold = data[i][0]
    return threshold


print(f([0.5, 0.8, 1.5, 2.1, 0.9], [0, 0, 1, 1, 0]))
