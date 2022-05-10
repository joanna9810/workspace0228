'''
래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
from collections import deque
# dfs 매서드 정리
def dfs(v):
    # 현재 노드를 방문 처리
    visit_list2[v] = 1
    print(v, end='')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n+1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)
#bfs
def bfs(v):
    # 방문해야 할 곳을 순서대로 넣을 큐
    q = deque()
    q.append(v)
    # dfs 를 완료한 visited (1로 되어있음)에서 0으로 방문체크
    visit_list[v] = 1
    # 큐 안에 데이터가 없을 떄 까지
    while q:
        v = q.popleft()
        print(v, end='')
        for i in range(1, n+1):
            if(visit_list[i] == 0 and graph[v][i] == 1):
                q.append(i)
                visit_list[i] = 1

# 각 노드가 연결된 정보를 표현
n, m, v= map(int, input().split())
# 인접 영행렬 생성
graph = [[0] * (n+1) for _ in range(n+1)]
# 방문한 곳 체크를 위한 배열
visit_list = [0] * (n+1)
# 입력 받은 두 값에 대해 영행렬에 1 삽입
visit_list2 = [0] * (n+1)

for _ in range(m):
   a,b = map(int, input().split())
   graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
