from sys import stdin
def reverse(lista,vacio):
    while len(lista) != 0:
        vacio.append(lista.pop())

    x = ""
    for i in range(len(vacio)):
        x += vacio[i]
    return x


def main():
    x = input()
    lista = []
    for i in range(len(x)):
        lista.append(x[i])
    print(reverse(lista,[]))
main()