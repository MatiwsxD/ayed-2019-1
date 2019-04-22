from sys import stdin
class Solution(object):
    def Perimetro_isl(self, cuadr):

        count = 0
        mapa, cuad = len(cuadr), len(cuadr[0])
        # go horizontal
        for i in range(mapa):
            for j in range(cuad):
                if j == 0 and cuadr[i][j] == 1:
                    count += 1
                if j == cuad - 1 and cuadr[i][j] == 1:
                    count += 1
                if j != cuad - 1:
                    count += abs(cuadr[i][j] - cuadr[i][j + 1])

        # go vertical:
        for j in range(cuad):
            for i in range(mapa):
                if i == 0 and cuadr[i][j] == 1:
                    count += 1
                if i == mapa - 1 and cuadr[i][j] == 1:
                    count += 1
                if i != mapa - 1:
                    count += abs(cuadr[i][j] - cuadr[i + 1][j])

        return count

if __name__ == "__main__":
    mapa = []
    while True:
        y = [int(j) for j in stdin.readline().split()]
        if y == [] :
            break
        mapa.append(y)
    xx = Solution()
    print(xx.Perimetro_isl(mapa))
