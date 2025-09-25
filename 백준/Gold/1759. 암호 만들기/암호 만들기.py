from itertools import combinations

N, M = map(int, input().split())
K = input().split()

chars = ('a', 'e', 'i', 'o', 'u')

K.sort()

for value in combinations(K, N):
    check = 0
    count = 0
    
    for K in value:
        if K in chars:
            check += 1
        else:
            count += 1
            
    if check >= 1 and count >= 2:
        print("".join(value))