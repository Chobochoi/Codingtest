import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
          

for i in range(n):
    m = int(input())
        
    while True:
        if m == 0 or m == 1:
            print(2)
            break
        if isPrime(m):
            print(m)
            break
        else:
            m+=1