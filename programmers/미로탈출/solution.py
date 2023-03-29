from collections import deque

def solution(maps):
    x, y = find_start_node(maps)
    start_pos = (x, y, 0)
    lever_pos = find_target_node(maps, start_pos, "L")
    exit = find_target_node(maps, lever_pos, "E")
    if exit[0] == -1 and exit[1] == -1:
        return -1

    return exit[2]


def find_start_node(maps: list) -> tuple:
    row_length = len(maps)
    col_length = len(maps[0])
    for i in range(row_length):
        for j in range(col_length):
            if maps[i][j] == "S":
                return (i, j)


def find_target_node(maps: list, start: tuple, target: str) -> tuple:
    if start[0] == -1 and start[1] == -1:
        return (-1, -1, -1)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    row_length = len(maps)
    col_length = len(maps[0])
    
    visited = [[False] * col_length for _ in range(row_length)]
    q = deque([(start[0], start[1], start[2])])
    visited[start[0]][start[1]] = True
    
    while q:
        x, y, cost = q.popleft()
        if maps[x][y] == target:
            return (x, y, cost)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row_length or ny < 0 or ny >= col_length:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == "X":
                continue
            q.append((nx, ny, cost+1))
            visited[nx][ny] = True
            
    return (-1, -1, -1)
