graph = []
n = int(input('Enter the number of lines: '))
for x in range(n):
    line = input(f'Enter the {x} graph line: ').split(' ')
    graph.append(line)

print(f'Graph: {graph}')

wordsToFind = []
x = int(input('Enter the number of words to find: '))
for x in range(x):
    word = input(f'Enter the {x} word: ')
    wordsToFind.append(word)
print(f'Words to find: {wordsToFind}')


def checkMove(x, y, graph, n):
    if 0 <= x < len(graph[0]) and 0 <= y < n:
        return True
    return False


m = len(graph[0])
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, 1, -1, -1, 0, 1]

for x in range(n):
    for y in range(m):
        moves = [(y + r, x + c) for r in row for c in col]
        for row, col in moves:
            if checkMove(col, row, graph, n):
                # do something
                print('')
            else:
                pass
