from sys import stdin
def busq(lista,item,cont):
    if len(lista)== 0:
        return -1
    else:
        if lista[len(lista)//2] == item:
            return cont+len(lista)//2
        else:
            if lista[len(lista)//2] > item:
                return busq(lista[:(len(lista)//2)],item,cont)
            else:
                return busq(lista[((len(lista)//2)+1):],item,cont+len(lista)//2)
def main():
    x = [int(i)for i in stdin.readline().split(",")]
    y = int(input())
    print(busq(x,y,1))
    
main()
