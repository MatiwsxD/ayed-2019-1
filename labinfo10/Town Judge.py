from sys import stdin
class Solution:
    def findJudge(self, N,trust):
        a = [0] * (N + 1)
        for l in trust:
            a[l[1]] += 1
            a[l[0]] -= 1

        for i in range(1, len(a)):
            if a[i] == N - 1:
                return i

        return -1

if __name__ == "__main__":
    mapa = []
    x = int(input())
    while True:
        y = [int(j) for j in stdin.readline().split()]
        if y == []:
            break
        mapa.append(y)
    xx = Solution()
    print(xx.findJudge(x,mapa))