n, k = map(int, input().split())
tower = list(map(int, input().split()))  # 0 - no tower; 1 - tower


def voisins(i):
    return range(min(n - 1, i + k - 1), max(-1, i - k), -1)


count = 0
past_fourni = 0
while past_fourni < n:
    for i in voisins(past_fourni):
        if tower[i]:
            past_fourni = i + k
            count += 1
            break
    else:
        count = -1
        break
print(count)
