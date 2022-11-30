def quickSort(m, left, right):
    if right - left <= 1:
        return m
    pivot = m[left]
    i = left + 1
    j = left + 1
    for j in range(j, right):
        if m[j] < pivot:
            m[j], m[i] = m[i], m[j]
            i += 1
        elif m[j] == pivot:
            m[j], m[i] = m[i], m[j]
    print(m)
    m[left], m[i - 1] = m[i - 1], m[left]
    m = quickSort(m, left, i - 1)
    m = quickSort(m, i, right)
    print(m)
    return m


def getMedian(list):
    length = len(list)
    if length <= 1:
        return list[0]
    elif length % 2 == 0:
        i = (length - 1) / 2
        return list[int(i)]
    else:
        i = (length) / 2
        return list[int(i)]


def getPivot(m):
    c = []
    i = 0
    while i <= len(m) - 1:
        tempList = []
        j = 0
        while j < 5 and i <= len(m) - 1:
            tempList.append(m[i])
            i = i + 1
            j = j + 1
        tempList = quickSort(tempList, 0, len(tempList) - 1)
        c.append(getMedian(tempList))
    c = quickSort(c, 0, len(c) - 1)
    medianOfMedians = getMedian(c)
    return medianOfMedians


def dSelect(m, position):
    pivot = getPivot(m)
    i = 0
    j = 0
    if len(m) <= 1:
        return m[0]
    for j in range(0, len(m)):
        if m[j] < pivot:
            m[j], m[i] = m[i], m[j]
            i += 1
        elif m[j] == pivot:
            m[j], m[i] = m[i], m[j]
        print("i: " + str(i))
        print("j: " + str(j))
    print("index of pivot: " + str(m.index(pivot)))
    print("pivot: " + str(pivot) + " list: " + str(m))
    if m.index(pivot) == position:
        return pivot
    elif m.index(pivot) > position:
        return dSelect(m[0:i], position)
    else:
        return dSelect(m[i:], position - i)


getMedian([10, 1, 1, 10, 5, 21])
