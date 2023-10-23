import sys
si = sys.stdin.readline
#INF = int(2e10)
#MX = 1000

n, x, c, p = map(int, si().split())
x -= 1
a = list(map(int, si().split()))
# ​C가 선행되어야 P를 만드는 조건?
# ​t 근처에서 조각 1개 만들어서 p비용 빌생하는 이유?
# x = 시작 하는  조각
# t 포함 숫자  마지막 조각
# x  오른쪽 
last, ans = a[0] + x, 0  # last초까지만 컴퓨터 작동함
for i in range(1, n):
    t = a[i]
    if t > last: # 마지막 조각으로 새로운 수 t 를 포함할 수 없는 상황
    
        ping_cnt = (t - last) // x # 횟수 : t -last //x 몫에다가
        if (t - last) % x > 0:
            ping_cnt += 1 #  나머지가 있으면 올림을 위해 +1
        
        ans += min(c, p * ping_cnt) # 연장 
    last = t + x
print(ans)
'''
7 30 5 2
0 29 59 90 122 500 600
=>
16
7 5 1 2
2 3 4 5 10 20 30
=>
3
'''
