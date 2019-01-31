from sys import stdin
def merge_sort(numbers): 
    n = len(numbers) 
    if(n == 1):
        return numbers 
 
    left = merge_sort(numbers[:(n//2)]) 
    right = merge_sort(numbers[(n//2):]) 
 
    return merge(left, right) 
 
def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
    len_left = len(left) 
    len_right = len(right)
    cont = 0
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
    return result

def main():
    lista = [int(x) for x in stdin.readline().split(",")]
    if len(lista)<= 10:
        print(*lista)
    else:
        x = merge_sort(lista)
        print(*x[-10:])
main()
