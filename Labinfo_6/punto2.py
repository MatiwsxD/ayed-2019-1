def countFriendsPairings(n):
    y = [0 for i in range(n + 1)] 
    for i in range(n + 1): 
        if i <= 2: 
            y[i] = i 
        else: 
            y[i] = y[i - 1] + (i - 1) * y[i - 2]   
    return y[n] 
def main():
    n = int(input())
    print(countFriendsPairings(n))
main()
