def main():
    n = int(input())
    lista = []
    for i in range(n+1):
        n = 1
        aux = []
        for j in range(i+1):
            aux.append(str(n)+ " " )
            n = int(n*(i-j)/(j+1))
        lista.append(aux)
        print()
    for i in (lista):
        print(*i)
main()
