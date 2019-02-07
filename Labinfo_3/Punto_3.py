def Huge_Fib(n,m):

    if n == 0 : return 0
    elif n == 1: return 1
    else:
        a,b = 0,1
        for i in range(1,n):
            a, b = b, (a+b) % m
        print(b);

def main():
    a= int(input())
    b = int(input())
    
    Huge_Fib(a,b)
main()
    
