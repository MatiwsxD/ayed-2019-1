from sys import stdin

"""def merge_sort(numbers): 
    n = len(numbers) 
    if(n == 1):
        return numbers 
 
    left = merge_sort(numbers[:(n//2)]) 
    right = merge_sort(numbers[(n//2):])
    
    return merge(left, right) 
 
def merge(left, right):
    global cont
    result = [] 
    i = 0 
    j = 0 
    len_left = len(left) 
    len_right = len(right)
    while(i < len_left or j < len_right):
        cont = cont +1
        if(i >= len_left): 
            result.append(right[j])
            j = j + 1 
        elif(j >= len_right): 
            result.append(left[i])
            i = i + 1 
        elif(left[i] < right[j]): 
            result.append(left[i])
            i = i + 1 
        else:
            result.append(right[j]) 
            j = j + 1
    
    return result"""
###Merge no sirve###

"""def max_multi(lista):
    global cont
    cont = cont+1
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
def min_multi(lista):
    global cont
    cont = cont+1
    if len(lista)==1:
        return lista[0]
    elif len(lista) == 2:
        if lista[0]< lista[1]:
            return lista[0]
        else:
            return lista[1]
    else:
        a = min_multi(lista[:len(lista)//2])
        b = min_multi(lista[(len(lista)//2)+1:])
        if a < b:
            return a
        else:
            return b"""
def max_min(lista,maxi,mini):
    global cont
    for i in lista:
        cont +=1
        if i > maxi:
            maxi = i
        else:
            mini = i
    return maxi,mini 
            
def main():
    global cont
    cont = 0
    #xx = int(input())
    x = [int(x) for x in stdin.readline().split(",")]
    y,z = max_min(x,x[1],x[1])
    print(y,z)
    print("total-Prmitido",cont,"-",3*len(x)/2)

main()

