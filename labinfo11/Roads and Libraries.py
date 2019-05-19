from collections import defaultdict, deque
for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    if x <= y:
        print(n * x)
        for _ in range(m):
            input()
    else:
        nbhd = defaultdict(list)
        for _ in range(m):
            c1, c2 = map(int, input().split())
            nbhd[c1].append(c2)
            nbhd[c2].append(c1)
        new_node = [True] * (n + 1)
        count = 0
        cache = deque()
        for cur in range(1, n + 1):
            if new_node[cur]:
                count += x
                cache.append(cur)
                new_node[cur] = False
                while cache:
                    for i in nbhd[cache.popleft()]:
                        if new_node[i]:
                            cache.append(i)
                            new_node[i] = False
                            count += y
        print(count)

