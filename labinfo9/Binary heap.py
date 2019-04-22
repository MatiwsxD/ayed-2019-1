from sys import stdin
def isHeap(arr, n):
    for i in range(int((n - 2) / 2) + 1):
        if arr[2 * i + 1] > arr[i]:
            return False
        if (2 * i + 2 < n and
                arr[2 * i + 2] > arr[i]):
            return False
    return True
if __name__ == '__main__':
    arr = [int(x) for x in stdin.readline().split()]
    n = len(arr)
    print(isHeap(arr, n))