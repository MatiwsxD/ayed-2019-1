nc = int(input())
for ca in range(nc):
    (n, m) = (int(t) for t in input().split())
    edges = [(int(t) - 1 for t in input().split()) for i in range(m)]
    s = int(input()) - 1
    fanout = [set() for i in range(n)]
    for (x, y) in edges:
        fanout[x].add(y)
        fanout[y].add(x)
    layer = [-1] * n
    bdd = {s}
    fog = set(range(n)).difference(bdd)
    idx = 0
    allBlocked = [-1] * n
    while len(bdd) > 0:
        for a in bdd:
            layer[a] = idx
    nextbdd = {f for f in fog if not bdd.issubset(fanout[f])}
    fog = fog.difference(nextbdd)
    bdd = nextbdd
    idx += 1
    print(' '.join(str(t) for t in layer if t > 0))
