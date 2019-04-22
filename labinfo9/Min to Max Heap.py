
from sys import stdin
def MaxHeapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, n)

def convertMaxHeap(arr, n):
    for i in range(int((n - 2) / 2), -1, -1):
        MaxHeapify(arr, i, n)

def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")

if __name__ == '__main__':
    arr = [int(x) for x in stdin.readline().split()]
    n = len(arr)
    convertMaxHeap(arr, n)
    printArray(arr, n)

