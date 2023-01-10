class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(data, root):
    if root is None:
        return Node(data)

    if root.data < data:
        root.right = insert(data, root.right)
    else:
        root.left = insert(data, root.left)

    return root


def PrintSorted(root, l):
    if root:
        PrintSorted(root.left, l)
        l.append(root.data)
        PrintSorted(root.right, l)
    return l


def find_closest(target, values):
    closest = None
    closest_diff = abs(target - values[0])

    for i in range(1, len(values)):
        diff = abs(target - values[i])

        if diff < closest_diff:
            closest_diff = diff
            closest = values[i]

    return closest


def main():
    value = int(input())
    n = int(input())
    values = []
    for i in range(n):
        values.append(int(input()))

    return value, values


if __name__ == '__main__':
    value, values = main()

    root = Node(values[0])
    for i in range(1, len(values)):
        root = insert(values[i], root)
    l = PrintSorted(root, [])
    print(find_closest(value, l))

# 19
# 8
# 5
# 14
# 4
# 6
# 8
# 7
# 24
# 22
