from sys import stdin
def mochila(x,y,n):
    if x == 0 or n == 0:
        return 0
    elif y [n-1]> x:
        return mochila(x,y,n-1)
    else:
        return max (mochila(x,y,n-1),1 + mochila(x - y[n-1],y,n-1))

    
def main():
    prec = [int(x) for x in stdin.readline().split(" ")]
    dine = int(input())
    print(mochila(dine,prec,len(prec)))
main()
