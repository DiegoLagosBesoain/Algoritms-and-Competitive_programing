import sys
sys.setrecursionlimit(10000)

t = int(input())

for _ in range(t):
    k, s = input().split()
    k = int(k)
    n = len(s) // k
    partitions = [set() for _ in range(n)]

    
    for i in range(n):
        for j in range(k):
            pos = i * k + j
            partitions[i].add(ord(s[pos]) - ord('a'))

    
    memo = [[-1 for _ in range(27)] for _ in range(n)]

    def solve(idx, last_char):
        if idx == n:
            return 0
        if memo[idx][last_char] != -1:
            return memo[idx][last_char]

        num_unique = len(partitions[idx])
        best = float('inf')

        for first in partitions[idx]:
            for last in partitions[idx]:
                if num_unique == 1 or first != last:
                    cost = solve(idx + 1, last) + num_unique
                    if last_char == first:
                        cost -= 1
                    best = min(best, cost)

        memo[idx][last_char] = best
        return best

    print(solve(0, 26))