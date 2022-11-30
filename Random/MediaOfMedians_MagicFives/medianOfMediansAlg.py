# from random import randrange
from statistics import median_grouped


# '/home/janek/PycharmProjects/PythonKlasa2/Random/MediaOfMedians_MagicFives/input.txt'


class Student:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def __lt__(self, other):
        return self.index < other.index

    def __float__(self):
        return float(self.index)


def inputs():
    # print('Robo Inputs:')
    with open('/home/janek/PycharmProjects/PythonKlasa2/Random/MediaOfMedians_MagicFives/input.txt', 'r') as file:
        input_lines = [line.strip() for line in file]
    # print(input_lines)

    k = input_lines[0]

    people = []

    for i in range(int(input_lines[1])):
        # people.append(input_lines[i + 2].split(' '))
        people.append(Student(input_lines[i + 2].split(' ')[0], input_lines[i + 2].split(' ')[1]))
    #     print(f'Name: {people[i].name}, Index: {people[i].index}')
    # print('\n')
    return k, people

    # print('Human Inputs:')
    # k = int(input())
    # k1 = int(input())
    # people = []
    # for i in range(k1):
    #     people.append(Student(input('Name: '), input('Index: ')))
    # return k, people


x = inputs()
people, k = x[1], x[0]


def start(people, k):
    if len(people) <= 3:
        people.sort(key=lambda x: x.index)
        print(people[2].name)
        print(people[2].index)
        return

    x = [[] for _ in range(int(len(people) / 5))]
    medians = []
    # medians
    for j in range(int(len(people) / 5)):
        for i in range(5):
            x[j].append(people[j + i])
        x[j].sort(key=lambda x: x.index)
        medians.append(median_grouped(x[j]))
        # something is wrong with the medians and I cant figure it out, in the first round the second value does not match the real median
    mdMd = median_grouped(medians)
    # print(f'Medians: {medians}')
    # print(f'Medians Of Medians: {mdMd}')
    L = []
    R = []

    for a in range(len(people)):
        if int(people[a].index) <= int(mdMd):
            L.append(people[a])
        else:
            R.append(people[a])
        # print(L)
        # print(R)

    if int(k) - len(L) <= 0:
        start(L, k - len(L))
    else:
        start(R, int(k) - len(R))


start(people, k)
