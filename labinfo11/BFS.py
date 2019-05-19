from collections import defaultdict, deque


def breadth_first_search(S, N, G, L = 1):
    E = defaultdict(int)
    C = {}

    for n in range(1, N + 1):
        C[n] = -1

    E[S] += 1
    C[S]  = 0
    Q     = deque([S])

    while Q:
        n = Q.popleft()
        for h in G[n]:
            if E[h] == 0:
                E[h] += 1
                C[h]  = C[n] + L
                Q.append(h)

    return C


def main():
    T = int(input())

    for _ in range(T):
        N, M = [int(i) for i in input().split()]

        G    = defaultdict(set)
        for _ in range(M):
            E = [int(i) for i in input().split()]
            G[E[0]].add(E[1])
            G[E[1]].add(E[0])

        S    = int(input())

        D    = breadth_first_search(S, N, G, 6)
        print(' '.join(str(D[n]) for n in range(1, N + 1) if n != S))


if __name__ == "__main__":
    main()