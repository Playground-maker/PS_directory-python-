# 빠른 출력

# import sys

# A = int(input())
# for i in range(A):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)




# 예쁘게 A + B 출력

# T = int(input())

# for i in range(1, T+1):
#     A, B = map(int, input().split())
#     print(f'Case #{i}: {A+B}')


# 더하기 사이클

# n = int(input())
# num = n
# cnt = 0

# while True:
#     a = num // 10
#     b = num % 10
#     c = (a + b) % 10
#     num = (b * 10) + c 
    
#     cnt += 1
#     if(num == n):
#         break
# print(cnt)    