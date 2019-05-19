import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse=True)
print(sum([2**j * calories[j] for j in range(n)]))