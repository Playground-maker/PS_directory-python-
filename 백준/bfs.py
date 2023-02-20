# BFS 

# BFS 알고리즘은 '너비 우선 탐색' 이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. 
# DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하는데, BFS는 그 반대다.
# 선입선출 방식인 큐 자료구조를 이용해 구현한다.
# 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 
# 가까운 노드부터 탐색을 진행하게 된다.

# 알고리즘의 정확한 동작 방식은 다음과 같다.

# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.

from collections import deque

def bfs(graph, start, visited):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  
  # 큐가 빌 때 까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end = ' ')
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

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

bfs(graph, 1, visited)




# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)


# 재귀함수

# def recursive_function(i):
#   if i == 10:
#     return
#   print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
#   recursive_function(i+1)
#   print(i, '번째 재귀 함수를 종료합니다')
  
# recursive_function(1)  


# def factorial_iterative(n):
#   result = 1
#   for i in range(1, n+1):
#     result *= i
#   return result 

# def factorial_recursive(n):
#   if n <= 1:
#     return 1
#   return n * factorial_recursive(n-1)

 