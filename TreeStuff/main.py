from random import randint


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


def PrintSorted(root):
    if root:
        PrintSorted(root.left)
        print(root.data)
        PrintSorted(root.right)


if __name__ == '__main__':
    root = Node(10)
    for r in range(10):
        b = randint(0, 100)
        # print(f'b: {b}')
        a = insert(b, root)

    PrintSorted(root)
