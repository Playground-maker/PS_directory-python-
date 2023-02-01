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



# 1차원 배열 갯수 세기

# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())

# print(n_list.count(v))


# 1차원 배열 -> X보다 작은 수

# N, X = map(int, input().split())
# n_list = list(map(int, input().split()))

# for i in range(N):
#     if n_list[i] < X:
#         print(n_list[i], end=' ')


# 과제 안 내신 분..?

# students = [i for i in range(1, 31)]

# for _ in range(28):
#     num = int(input())
#     students.remove(num)
    
# print(min(students))
# print(max(students))


# a = 123
# print(sum(map(int, str(a))))



# import sys

# def recursion(s, l, r):
#     global cnt
#     cnt += 1
#     if l >= r: return 1
#     elif s[l] != s[r]: return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)

# n = int(input())
# for _ in range(n):
#     cnt = 0
#     print(isPalindrome(sys.stdin.readline().rstrip()), cnt)