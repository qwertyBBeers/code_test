N = int(input())
a = [0] * 201  # -100부터 100까지 총 201개

nums = list(map(int, input().split()))

for num in nums:
    a[num + 100] += 1  # 인덱스 보정: -100 → 0, 0 → 100, 100 → 200

x = int(input())  # 찾고자 하는 수
print(a[x + 100])  # x가 등장한 횟수 출력