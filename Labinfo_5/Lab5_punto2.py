from sys import stdin


def main():
    lista = [[0,0,0],
         [0,1,0],
         [0,0,0]]
    cont = 0
    x = 0
    y = 0
    while True:
        if y == -1:
            print(cont)
            break
        if 0 <= x <lista[y] and lista[y][x+1]==0:
            lista[y][x] =1
            x+=1
        if lista[y][x+1] ==1 and lista[y+1][x] == 0:
            lista[y][x] =1
            y +=1
        if lista[y][x+1] == 1 and lista[y+1][x] == 1:
            lista[x][y]
            x-=1
        if len(lista)==y+1 and len(lista[0]==x+1):
            x =0
            y = 0
            cont+=1
         

    
