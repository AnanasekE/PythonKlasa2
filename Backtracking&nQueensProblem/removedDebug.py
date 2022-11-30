def check(t, x, y):
    for i in range(x):
        xDiff = abs(i - x)
        yDiff = abs(t[i] - y)
        if y == t[i] or xDiff == yDiff:
            return False
    return True


def main(t, n):
    count = 0
    if len(t) == n:
        return 1
    else:
        for i in range(n):

            if check(t, len(t), i):
                t.append(i)
                count += main(t, n)
                t.pop()
    return count


n = int(input())
t = []
print(main(t, n))
