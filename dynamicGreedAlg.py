backpackSize = int(input())
itemsAmount = int(input())
items = [[int(x) for x in input().split()] for _ in range(itemsAmount)]  # [[weight, value], [weight, value] ...]

print(items)

count = [0 for _ in range(backpackSize + 1)]

for i in range(len(items)):
    for j in range(items[i][1], backpackSize + 1):
        if j >= items[i][1]:
            count[j] = max(count[j], items[i][0] + count[j - items[i][1]])

print(count)
print(count[backpackSize])
