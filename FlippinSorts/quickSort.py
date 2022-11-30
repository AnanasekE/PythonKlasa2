def Pivot(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def QuickSort(arr, low, high):
    if low < high:
        pi = Pivot(arr, low, high)
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)


arr = [7, 1, 8, 9, 2, 6, 5]
QuickSort(arr, 0, len(arr) - 1)
print(f'Sorted array: {arr}')

# x = input().split()
x = "6 4 3".split()
print(x)
boxCount = int(x[0])
packageCount = int(x[1])
c = int(x[2])

for _ in range(boxCount):
    w = input()
    w.split()
