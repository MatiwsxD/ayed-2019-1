from sys import stdin
def rotation(lista,y):
    if y == 0:
        return lista
    else:
        x =lista[0]
        lista = lista[1:]
        z = lista+[x]
        return rotation(z,y-1)

def main():
    x = [int(x) for x in stdin.readline().strip(" ").split()]
    y = int(input())
    print(rotation(x,y))
main()