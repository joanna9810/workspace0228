from collections import deque


# 이동할 방향 정의 (상,하,좌,우,대각선)
dx = [-1,1,0,0,-1,+1,-1,+1]
dy = [0,0,-1,1,-1,-1,+1,+1]
# BFS 소스 구현
def bfs(y, x):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((y,x))
    # 큐가 빌때까지 무한 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어나는 경우 무시
            if nx < 0 or nx >= w or ny <0 or ny >=h:
                continue
            # 바다인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
# w, h 정보 받기
while True:
    h, w = map(int, input().split())
    if w == 0 or h == 0:
        break
    # 2차원 리스트의 맵 정보 받기
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
# 가장 오른쪽 아래까지의 최단 거리 반환

result = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            result += 1
            bfs(i,j)
print(result)