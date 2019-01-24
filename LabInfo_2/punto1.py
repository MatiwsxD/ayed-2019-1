from sys import stdin
def max_multi(lista):
    if len(lista)==1:
        return lista[0]
    elif len(lista) == 2:
        if lista[0]> lista[1]:
            return lista[0]
        else:
            return lista[1]
    else:
        a = max_multi(lista[:len(lista)//2])
        b = max_multi(lista[(len(lista)//2)+1:])
        if a > b:
            return a
        else:
            return b
def main():
    x = [int(i)for i in stdin.readline().split(",")]
    y = max_multi(x)
    z = x.index(y)
    w = x.pop(z)
    a = max_multi(x)
    print(y*a)
main()
