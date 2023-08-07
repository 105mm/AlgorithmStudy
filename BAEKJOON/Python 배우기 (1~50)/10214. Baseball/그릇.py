a = int(input())
for _ in range(a):
    y_score=0
    g_score=0
    
    
    for _ in range(9):
        y, g = map(int, input().split())
        
        if y>g:
            y_score += y
            
        if y<g:
            g_score += g
        
        else:
            pass

    if y_score > g_score:
        print("Yonsei")

    if y_score < g_score:
        print("Korea")

    if y_score == g_score:
        print("Draw")