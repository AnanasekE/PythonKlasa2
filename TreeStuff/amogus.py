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
        print(root.name)
        PrintSorted(root.right)


def Remove(root, low, high):
    if root is None:
        return None
    root.left = Remove(root.left, low, high)
    root.right = Remove(root.right, low, high)

    if root.data.mean < low:
        root = root.right
        print(f'root: {root}') # problem is here (root.data.mean) is None
    if root.data.mean > high:
        root = root.left

    return root


def main():
    with open('input.txt', 'r') as file:
        input_lines = [line.strip() for line in file]

    count = input_lines[0]
    money = list(map(int, input_lines[1].split(' ')))
    companies = []
    for i in range(0, int(count) * 2, 2):
        nums = input_lines[i + 3].split(' ')
        companies.append(Company(input_lines[i + 2].split(' ')[0], list(map(int, nums))))
    return count, money, companies


if __name__ == '__main__':
    count, money, companies = main()
    # print(f'Count: {count}, Money: {money}, Companies: {companies}')
    # for g in companies:
    #     print(f'Name: {g.name}, Prices: {g.prices}, Mean: {g.mean}')

    # root = Node(10)
    # for r in range(10):
    #     b = randint(0, 100)
    #     # print(f'b: {b}')
    #     a = insert(b, root)
    # PrintSorted(root)

    root = Node(companies[0], companies[0].name)
    for i in range(1, len(companies)):
        root = insert(companies[i], root, companies[i].name)
    PrintSorted(root)
    print('-----------------')
    root = Remove(root, money[0], money[1])
    PrintSorted(root)
