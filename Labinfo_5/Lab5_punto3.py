from sys import stdin
def change (cambio,monedas,lista):
    if sum(lista)==cambio:
        yield lista
    elif sum(lista)> cambio:
        pass
    elif monedas == []:
        pass
    else:
        for o in change(cambio,monedas[:],lista+[monedas[0]]):
            yield o
        for j in change(cambio,monedas[1:],lista):
            yield j
def main():
    cambio = int(input())
    monedas = [int(x) for x in stdin.readline().strip(" ").split()]
    sol =[s for s in change(cambio,monedas,[])]
    print(sol)
    for s in sol:
        print(*s)
main()
