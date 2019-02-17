from sys import stdin
def primo(x):
    print(x)
    lista = [2,3,5,7]
    for i in lista:
        if x **(1/2) == int(x **(1/2)):
            return "No"
        elif i == x:
            return "Si"
        elif x%i == 0:
            return "No"
    else:
        return "Si"
def main():
    x = int(input())
    y = [int(x) for x in stdin.readline().strip(" ").split()]
    for i in y:
        print(primo(i))
main()
