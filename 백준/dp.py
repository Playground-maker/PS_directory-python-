# 다이나믹 프로그래밍

# 1로 만들기 - 연산을 하는 횟수의 최솟값을 출력하기

# x = int(input())
# d = [0] * 10001

# for i in range(2, x + 1):
#   # 현재의 수에서 1을 빼는 경우
#   d[i] = d[i - 1] + 1
#   # 현재의 수가 2로 나누어 떨어지는 경우
#   if i % 2 == 0:
#     d[i] = min(d[i], d[i // 2] + 1)
#   # 현재의 수가 3으로 나누어 떨어지는 경우
#   if i % 3 == 0:
#     d[i] = min(d[i], d[i // 3] + 1)
#   # 현재의 수가 5로 나누어 떨어지는 경우
#   if i % 5 == 0:
#     d[i] = min(d[i], d[i // 5] + 1)
  
# print(d[x])      


# 개미 전사 - 개미 전사가 얻을 수 있는 식량의 최댓값 출력

# n = int(input())
# # 모든 식량 정보 입력받기
# array = list(map(int, input().split()))

# # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [0] * 100

# # 다이나믹 프로그래밍 진행(보텀업) 
# d[0] = array[0]
# d[1] = max(array[0], array[1]) 

# for i in range(2, n):
#   d[i] = max(d[i - 1], d[i - 2] + array[i])

# print(d[n - 1])  
  

# 효율적인 화폐 구성
n, m = map(int, input().split())
array = []

for i in range(n):
  array.append(int(input()))
  
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
  # 각각의 화폐 단위 i
  for j in range():
    # 각각의 금액 j     
    
    d




# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
# d = [0] * 100
# 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 호출하면 메모한 결과를 그대로 가져오는
# 기법임. 캐싱이라고 부르기도 함
# 피보나치 함수를 구현해보자(탑다운 다이나믹 프로그래밍)
# def fibo(x):
#   if x == 1 or x == 2:
#     return 1
#   # 이미 계산한 적 있는 문제라면 그대로 반환
#   if d[x] != 0:
#     return d[x]
#   d[x] = fibo(x - 1) + fibo(x - 2)
#   return d[x]

# print(fibo(99))



#피보나치 수열 소스코드(반복문 이용, 보텀업 방식)
# d = [0] * 100
# d[1] = 1
# d[2] = 2
# n = 99

# for i in range(1, n+1):
#   d[i] = d[i - 2] + d[i - 1]
  
# print(d[n])
  


# 피보나치 함수를 재귀 함수로 구현 - 굉장히 비효율적임

# def fibo(x):
#   if x == 1 or x == 2:
#     return 1
#   return fibo(x - 1) + fibo(x - 2)

# print(fibo(4))


