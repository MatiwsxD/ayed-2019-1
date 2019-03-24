from sys import stdin
def diference(x):
    y = [int(i) for i in range(1,len(x))]
    lista = []
    for i in range (len(x)-1):
        m = abs(x[i]-x[i+1])
        lista.append(m)
    lista = sorted(lista)
    if y == lista:
        print(True)
    else:
        print(False)


def main():
    x = [int(x) for x in stdin.readline().strip(" ").split()]
    diference(x)
main()