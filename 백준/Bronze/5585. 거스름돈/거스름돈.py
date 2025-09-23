M = int(input())
N = 1000 - M

change = [500, 100, 50, 10, 5, 1]

index = 0
total = 0
      
while N > 0:
    if N % change[index] != 0 and change[index] > N % change[index] :
        total = total + N // change[index]
        N = N % change[index]
        index += 1
    elif N % change[index] == 0:
        total = total + N // change[index]
        break    
           
print(total)