from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 도시의 도로 정보 받기
for _ in range(1, n+1):
    a,b = map(int,input().split())
    graph[a].append(b)

# 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

# 너비우선 탐색
q = deque([x])
while q:
    now = q.popleft()
    #현재 도시에서 이동가능한 모든 도시 확인
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

#최단 거리가 k 인 도시를 오름 차순으로 출력
Check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        Check = True
if Check == False:
    print(-1)