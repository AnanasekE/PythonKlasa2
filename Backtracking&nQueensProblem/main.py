def check(t, x, y):
    for i in range(x):
        xDiff = abs(i - x)
        yDiff = abs(t[i] - y)
        print(f'xDiff: {xDiff}, yDiff: {yDiff}')
        print(f'y: {y}, t[i]: {t[i]}, i: {i}')
        if y == t[i] or xDiff == yDiff:
            return False
    return True


def main(t, n):
    print(f't: {t}, n: {n}')
    count = 0
    if len(t) == n:
        return 1
    else:
        for i in range(n):
            print(check(t, len(t), i))
            if check(t, len(t), i):
                t.append(i)
                count += main(t, n)
                t.pop()
    return count


n = 4
t = []
print(main(t, n))
