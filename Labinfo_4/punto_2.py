from sys import stdin
def parejas(x):
    lista = []
    for i in x:
        for j in range(len(x)):
            if i[0] == x[j][0] or i[0] == x[j][1] or x[1] == x[j][0] or x[1] == x[j][1] and i != x[j]:
                lista += x[j]
                
    return lista
def main():
    lista_1 = []
    x = int(input())
    for i in range(x):
        y = [int(x) for x in stdin.readline().strip(" ").split()]
        lista_1.append(y)
    print(parejas(lista_1))
main()
