import sys
input = sys.stdin.readline

def cut_line(start, end):
    if end == 1:
        return
    
    for i in range(start + end//3, start + (end//3 * 2)):
        ST[i] = ' '
        
    cut_line(start, end//3)
    cut_line(start + (end//3 * 2), end//3)
    

while True:
    try:
        N = int(input())
        ST = ['-'] * (3 ** N)
        cut_line(0, 3**N)
        print(''.join(ST))
    except:
        break