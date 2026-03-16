def solution(sizes):
    w = []
    h = []
    
    for card in sizes:
        w.append(max(card))
        h.append(min(card))
        
    return max(w) * max(h)