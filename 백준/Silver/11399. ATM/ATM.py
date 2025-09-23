N = int(input())
M = list(map(int, input().split()))

M.sort()

sum_st = []
total = 0

for i in range(len(M)):
    total += M[i] * (len(M) - i)
  
print(total)