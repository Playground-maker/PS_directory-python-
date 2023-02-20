# dfs 풀이(코테)

# DFS는 깊이 우선 탐색 알고리즘으로, 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한
# 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘이다.
# 스택 구조를 이용하며, 구체적인 동작 과정은 다음과 같다.

# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은
#  인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

# (방문 처리는 스택에 한번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것을 의미한다. 방문 처리를 함으로써 각 노드를 한 번씩만 처리할 수 있다.)

def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end = ' ')
  
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)




# Adjacency matrix - graph

# INF = 99999999

# graph = [
#   [0, 7, 5], 
#   [7, 0, INF],
#   [5, INF, 0]
# ]

# print(graph)


# Adjacency list - graph

# # 행이 3개인 2차원 리스트로 인접 리스트 표현
# graph = [[] for _ in range(3)]

# # 노드 0에 연결된 노드 정보 저장(노드, 거리)
# graph[0].append((1, 7))
# graph[0].append((2, 5))

# # 노드 1에 연결된 노드 정보 저장
# graph[1].append((0, 7))

# # 노드 2에 연결된 노드 정보 저장
# graph[2].append((0, 5))

# print(graph)




# <스택 자료구조>

# stack = []
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack)
# print(stack[::-1])