graph = []
n = int(input('Enter the number of lines: '))
for x in range(n):
    line = input(f'Enter the {x} graph line').split(' ')
    graph.append(line)

print(f'Graph: {graph}')

wordsToFind = input().split(' ')
print(f'Words to find: {wordsToFind}')
