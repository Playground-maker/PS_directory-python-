# 한번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100
# 한번 구한 결과를 메모리 공간에 메모해두고 같은 식을 호출하면 메모한 결과를 그대로 가져오는
# 기법임. 캐싱이라고 부르기도 함
# 피보나치 함수를 구현해보자(탑다운 다이나믹 프로그래밍)
def fibo(x):
  if x == 1 or x == 2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

print(fibo(99))



# 피보나치 함수를 재귀 함수로 구현 - 굉장히 비효율적임

# def fibo(x):
#   if x == 1 or x == 2:
#     return 1
#   return fibo(x - 1) + fibo(x - 2)

# print(fibo(4))


