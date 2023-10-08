import sys
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    N, X, Y = map(int, input().split())
    walls = []
    for _ in range(N):
        x1, y1, x2, y2, C = map(int, input().split())
        walls.append(((x1, y1), (x2, y2), C))
    
    # Add the distance between the nuclear facility and walls to the walls list
    for i in range(N):
        dist = min(
            calculate_distance(walls[i][0], (X, Y)),
            calculate_distance(walls[i][1], (X, Y))
        )
        walls[i] = (walls[i][0], walls[i][1], walls[i][2], dist)
    
    # Sort walls by the distance to the nuclear facility
    walls.sort(key=lambda x: x[3])
    
    total_cost = 0
    selected_walls = []
    
    for wall in walls:
        x1, y1, x2, y2, C, dist = wall
        if all(calculate_distance((x1, y1), (x, y)) >= dist for x, y, _, _, _, _ in selected_walls):
            selected_walls.append((x1, y1, x2, y2, C, dist))
            total_cost += C
    
    if len(selected_walls) == N:
        print(total_cost)
    else:
        print(-1)

if __name__ == "__main__":
    main()
