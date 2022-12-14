def IsAnagram():
    word = input().split(' ')
    word1 = word[0]
    word2 = word[1]
    letters = {}
    # dodaje litery z pierwszego słowa do słownika
    for letter in word1:
        letters[letter] = letters.get(letter, 0) + 1

    # odejmuje litery z drugiego słowa od słownika
    for letter in word2:
        if letter in letters:
            letters[letter] -= 1
    for letter in letters:
        if letters[letter] != 0:
            return False
    return True


# reszta kodu
count = int(input())
values = []
for _ in range(count):
    values.append(IsAnagram())

for value in values:
    if value:
        print(True)
    else:
        print(False)
