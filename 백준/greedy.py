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

    
