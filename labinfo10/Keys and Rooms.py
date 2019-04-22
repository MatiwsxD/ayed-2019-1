from sys import stdin
class solucion(object):
    def canVisitAllRooms(self, rooms):
        visitado = [False] * len(rooms)
        visitado[0] = True
        stack = [0]
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not visitado[i]:
                    visitado[i] = True
                    stack.append(i)
        return all(visitado)


if __name__ == "__main__":
    rooms = []
    x = int(input())
    for i in range(x):
        y = [int(j) for j in stdin.readline().split()]
        rooms.append(y)
    xx = solucion()
    print(xx.canVisitAllRooms(rooms))