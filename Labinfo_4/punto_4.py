from sys import stdin
def insertionSort(alist):
    cont = 0
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        cont +=1
        alist[position]=currentvalue
    return cont
def main():
    alist = [int(x) for x in stdin.readline().split(" ")]
    print(insertionSort(alist))
main()
