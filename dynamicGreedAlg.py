# backpackSize = int(input())  # wilkość plecaka
# itemsAmount = int(input())  # ilość przedmiotów
import random

itemsAmount = 3
backpackSize = 5

# input wartość waga
items = [[8, 2], [5, 1], [4, 3]]
best = [0 for _ in range(backpackSize)]
lastBest = [0 for _ in range(backpackSize)]
print("best: ", best)
print('lastBest: ', lastBest)
for i in items:
    for j in range(backpackSize + 1):
        if j >= i[1]:
            print(lastBest[j], i[1 - lastBest[j]])
            if lastBest[j] >= i[0]:
                # print(lastBest[j], i[0])
                pass
                # x = i[0] + (lastBest[j - i[1]])

