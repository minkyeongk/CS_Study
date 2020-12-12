# 처음에는 파이썬 활용해서 풀고 stl없이 풀길 바라는 경우 다른 알고리즘 사용

# 배열 회전 알고리즘 1: 파이썬 pop 활용
arr = [1, 2, 3, 4, 5, 6, 7]
print(len(arr))     # 배열 길이 출력

n = 2   # 회전 횟수
# 파이썬 리스트는 pop 사용하면 되지만 cpp는 일일히 한칸씩 당겨줘야 함

print(arr)
for _ in range(n):
    arr.append(arr.pop(0))      # 효율성이 가장 안좋을 듯

print(arr)

# 배열 회전 알고리즘 2: 파이썬 슬라이싱
arr = [1, 2, 3, 4, 5, 6, 7]
print(len(arr))     # 배열 길이 출력

n = 2   # 회전 횟수

n %= len(arr)
result = arr[n:]+arr[:n]
print(result)


# 배열 회전 알고리즘 3: 저글링 알고리즘, 왼쪽으로
# gcd가 아니라 베수일 때로 생각
# 한 턴의 마지막 인자는 temp에 미리 넣어둔 값을 넣음
# 횟수는 len을 n으로 나눠서 계산
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l = len(arr)
n = 3

if l % n == 0:    # 저글링 알고리즘 가능
    base = 0     # < < < 마지막에 >
    m = l//n     # 반복 횟수를 알기 위함

    for i in range(n):  # 큰 반복은 옮기고자 하는 인자 개수지
        idx = base
        temp = arr[base]    # 마지막 인자를 위한
        for _ in range(m-1):
            arr[idx] = arr[idx+n]   # 값을 넣어주는게 다음 넣는거에 영향을 미치지 않도록 방향 설정
            idx += n
        arr[l-n+base] = temp
        base += 1   # 다음 단위로

print(arr)

# 배열 회전 알고리즘 3: 역전 알고리즘
# 기능 상으로 스플라이싱을 구현하는데 굳이 역전 알고리즘을 한번 더 사용할 필요가 있을까?
arr = [1, 2, 3, 4, 5, 6, 7]
n = 2

def reverse(arr):
    l = len(arr)
    last = l-1
    for i in range(0, l//2):
        temp = arr[i]
        arr[i] = arr[last-i]
        arr[last-i] = temp
    return arr

# 스플라이싱 구현은 그냥 append 반복하면 되니까
print(reverse(reverse(arr[:2])+reverse(arr[2:])))

# 배열의 특정 최대합 구하기
arr = [1, 20, 2, 10]
l = len(arr)
Bsum = 0

for _ in range(l):
    Lsum = 0
    for i in range(l):
        Lsum += i*arr[i]
    if Bsum < Lsum:
        Bsum = Lsum
    arr.append(arr.pop(0))
print(Bsum)

# 특정 배열을 arr[i] = i로 재배열 하기
arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]

for i in range(len(arr)):
    if arr[i] != i and arr[i] != -1:
        x = arr[i]
        while arr[x] != x and arr[x] != -1:
            y = arr[x]
            arr[x] = x
            x = y
    # 돌아갈거 다 돌아가고 원래 자리로 돌아와서 얘는 값이 있는지 확인
    if arr[i] != i:
        arr[i] = -1
print(arr)









