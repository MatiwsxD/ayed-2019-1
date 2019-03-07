from collections import defaultdict
keys = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 ['*', 0, '#'],
]
row = [0, -1, 0, 1]
col = [-1, 0, 1, 0]
def fill_keypad_map():
    def is_valid(i, j):
        if 0 <= i <=3 and 0 <= j <=2 and keys[i][j] != "#" and keys [i][j] != "*":
            return True 
    keypad_map = defaultdict(list)
    for i in range(4):
        for j in range(3):
            for k in range(4):
                r = i + row[k]
                c = j + col[k]
                if is_valid(i, j) and is_valid(r, c):
                    keypad_map[keys[i][j]].append(keys[r][c])
    return keypad_map
def keypad(n):
    keypad = fill_keypad_map()
    return keypad
def main():
    n = int(input())
    count = keypad(n)
    #print(f'Combinations: {count}')
    #print(count[5])
    combination(count,n)

def combination(count,n):
    matriz = []
    for i in range(10):
        matriz += [[1]+[0]*(n-1)]
##    print(matriz)
    for j in range(1,len(matriz[1])):
        for k in range(len(matriz)):
            y = count[k]+[k]
##            print(y)
            for l in y:
                
                matriz[k][j] += matriz[l][j-1]
##    for a in matriz:
##        print(a)
                
##            print(matriz[k][j])
##            print("Filas",k,"Columnas",j)
    cont = 0
    for i in matriz:
        cont+=i[-1]
    print(cont)
                
##    print(matriz)            
main()            

