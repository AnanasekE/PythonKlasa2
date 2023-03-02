def start():
    graph1 = []
    # inputs
    lineAmount = int(input('Enter the number of lines: '))

    for numberOfWords in range(lineAmount):
        line = input(f'Enter the {numberOfWords} graph line: ').split(' ')
        graph1.append(line)

    print(f'Graph: {graph1}')

    words = []
    numberOfWords = int(input('Enter the number of words to find: '))

    for numberOfWords in range(numberOfWords):
        word = input(f'Enter the {numberOfWords} word: ')
        words.append(word)

    print(f'Words to find: {words}')
    return graph1, words, lineAmount


def checkMove(x, y, visited) -> bool:
    if (0 <= x < m) and (0 <= y < n) and not visited[y][x]:
        return True
    return False


def WalkThroughVertex(x, y, visited, result):
    result += str(graph[y][x])
    if result in wordsToFind:
        print(f'Found word: {result}')
    visited[y][x] = True
    adjacent_vertex_indices = [
        (y + row[i], x + col[i])
        for i in range(len(row))
        if checkMove(x + col[i], y + row[i], visited)
    ]
    for new_y, new_x in adjacent_vertex_indices:
        WalkThroughVertex(new_x, new_y, visited, result)


graph, wordsToFind, n = start()

m = len(graph[0])

# define available moves
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, 1, -1, -1, 0, 1]

# start checking
for x in range(n):
    for y in range(m):
        result = ''
        visited = [[False for _ in range(m)] for _ in range(n)]
        WalkThroughVertex(x, y, visited, result)
