from sys import stdin
def main():
    lista = [[0,0,0],
         [0,1,0],
         [0,0,0]]
    x = 0
    j = 0
    cont = 0
    while x != -1:
        if lista[x+1][j] == 0:
            x = 1
            lista[x][j]=1
        elif lista[x+1][j] ==1 and lista[x][j+1]==0:
            j+=1
        elif lista[x+1][j] == 1 and lista[x][j+1] ==1:
            x -= 1
        

                
    
