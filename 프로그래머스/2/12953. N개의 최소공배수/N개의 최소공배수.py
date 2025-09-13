import math

def fuction(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    n = arr[0]
    for i in arr[1:]:
        n = fuction(n, i)
    return n
    
    
    