from sys import stdin 
keys =[[1,2,3],
       [4,5,6],
       [7,8,9],
       ['*',0,'#'],]

row =[0,-1,0,1]
col =[-1,0,1,0]
pos_filas = [0,1,2,3,4,5,6,7,8,9]
def cadenas(pos_fil,pos_colum,longitud):
    if longitud == 1:
        return keys[pos_fil][pos_colum]
    else:
        for i in range(len(row)):
            return " "+ keys[cadenas(pos_fil+row[i],pos_colum+pos[colum],longitud-1)]
def algo(longitud):
    for i in range(pos_fila):
        for j in range(pos_fila):
            cadenas(i,j,longitud)
longitud = 4
    
