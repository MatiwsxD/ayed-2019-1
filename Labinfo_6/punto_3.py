def domino(n): 
  
    list_1 = [0] * (n + 1) 
    list_2 = [0] * (n + 1) 
    list_1[0] = 1
    list_1[1] = 0
    list_2[0] = 0
    list_2[1] = 1
    for i in range(2, n+1): 
        list_1[i] = list_1[i - 2] + 2 * list_2[i - 1] 
        list_2[i] = list_1[i - 1] + list_2[i - 2] 
      
    return list_1[n] 

def main():  
    n = int(input())
    print(domino(n))
main()
