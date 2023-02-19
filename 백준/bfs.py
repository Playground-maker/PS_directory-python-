# BFS 







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

 