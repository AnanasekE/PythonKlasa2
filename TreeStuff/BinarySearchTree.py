import statistics


class Company:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices
        self.mean = statistics.mean(prices)

    def __lt__(self, other):
        return self.mean < other.mean


class Node:
    def __init__(self, data, name):
        self.data = data
        self.left = None
        self.right = None
        self.name = name


def insert(data, root, name):
    if root is None:
        return Node(data, name)

    if root.data < data:
        root.right = insert(data, root.right, name)
    else:
        root.left = insert(data, root.left, name)

    return root


def PrintSorted(root):
    if root:
        PrintSorted(root.left)
        print(root.name, root.data.mean)
        PrintSorted(root.right)


def Remove(root, low, high):
    if root is None:
        return None
    root.left = Remove(root.left, low, high)
    root.right = Remove(root.right, low, high)

    if root.data.mean < low:
        root = root.right
    elif root.data.mean > high:
        root = root.left

    return root


def main():

    count = int(input())
    money = list(map(int, input().split(' ')))
    companies = []
    for i in range(count):
        name = input()
        nums = input().split(' ')
        companies.append(Company(name, list(map(float, nums))))

    return count, money, companies


if __name__ == '__main__':
    count, money, companies = main()

    root = Node(companies[0], companies[0].name)
    for i in range(1, len(companies)):
        root = insert(companies[i], root, companies[i].name)
    PrintSorted(root)
    print()
    root = Remove(root, money[0], money[1])
    PrintSorted(root)
