import sys
input = sys.stdin.readline


while True:
    N = int(input())
    if N == -1:
        break
    ST = []
    for i in range(1, N):
       if N % i == 0:
           ST.append(i)
    
    if sum(ST) == N:
        print(N, " = ", " + ".join(str(i) for i in ST), sep="")
    else:
        print(N, "is NOT perfect.")    