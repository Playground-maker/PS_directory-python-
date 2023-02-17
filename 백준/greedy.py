# 거스름돈 문제

# n = 1260
# count = 0

# coin_types = [500, 100, 50, 10]
# for coin in coin_types:
#   count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 갯수 세기
#   n %= coin
  
# print(count)  


# 모험가 길드 문제

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data:
#   count += 1
#   if count >= i:
#     result += 1
#     count = 0
    
# print(result) 



# 1이 될 때 까지 case 1

# n, k = map(int, input().split())
# result = 0

# while True:
#   target = (n//k) * k
#   result += (n - target)
#   n = target
  
#   if n < k:
#     break
  
#   result += 1
#   n = n // k
  
# result = result + (n - 1)
# print(result)  


# case 2

# n, k = map(int, input().split())
# result = 0

# while n >= k:
  
#   while n % k != 0:
#     n = n - 1
#     result += 1
  
#   n = n // k
#   result += 1
  
# while n > 1:
#   n = n - 1
#   result += 1
  
# print(result)    



