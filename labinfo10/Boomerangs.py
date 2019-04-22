
from sys import stdin
class solucion:
    def boomerangs(self, puntos):
        # Write your code here
        count = 0
        for i in puntos:
            d = {}
            for m in puntos:
                if i == m:
                    continue
                dist = self.dis_punt(i, m)
                countofdist = d.get(dist, 0)
                d[dist] = countofdist + 1
            for dist in d:
                count += d[dist] * (d[dist] - 1)

        return count

    def dis_punt(self, x, y):
        return (x[1] - y[1]) ** 2 + (x[0] - y[0]) ** 2

if __name__ == "__main__":
    mapa = []
    x = int(input())
    for i in range (x):
        y = [int(j) for j in stdin.readline().split()]
        if y == [] :
            break
        mapa.append(y)
    xx = solucion()
    print(xx.boomerangs(mapa))