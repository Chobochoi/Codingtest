import sys

input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

total_cost = 0
min_price = oils[0]

for i in range(N-1):
    total_cost += min_price * roads[i]     
    
    min_price = min(min_price, oils[i+1])
    
print(total_cost)