def FindPairs(numbers, target):
    dict = {}
    for i in range(len(numbers)):
        difference = target - numbers[i]
        if difference in dict:
            print([dict[difference], i])
        else:
            dict[numbers[i]] = i


def FindPairs2(numbers, target):
    Pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                Pairs.append((numbers[i], numbers[j]))
    return Pairs


target = int(input())
nums = list(map(int, input().split(' ')))

print(FindPairs(nums, target))