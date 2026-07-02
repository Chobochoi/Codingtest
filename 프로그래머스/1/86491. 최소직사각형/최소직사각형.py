def solution(sizes):
    max_width = 0
    max_height = 0
    
    for w, h in sizes:
        # 두 변 중 긴 쪽을 width, 짧은 쪽을 height로 간주하여 최대값 갱신
        max_width = max(max_width, max(w, h))
        max_height = max(max_height, min(w, h))
        
    return max_width * max_height