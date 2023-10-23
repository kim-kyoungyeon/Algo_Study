# 2. 
import sys
from collections import deque
si = sys.stdin.readline
n= int(si())
inp = []
edges =[[] for _ in range(n)]
con = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n -1):
    x,y = map(int,si().split())
    x -=1
    y -=1
    inp.append((x,y))
    edges[x].append(y)
    edges[y].append(x)
    con[x][y] =1
    con[y][x] =1
ans = n -1

def bfs(x,visit):
    q = deque()
    q.append(x)
    visit[x] = True
    sz= 1
    while q:
        x = q.popleft()
        for y in edges[x]:
            if not visit[y] and con[x][y] ==1:
                q.append(y)
                visit[y] = True
                sz +=1
    return sz

def solve():
    visit = [False for _ in range(n)]
    sizes =[]
    for i in range(n):
        if not visit[i]:
            sizes.append(bfs(i,visit))
    assert len(sizes) == 3
    return max(sizes) - min(sizes)

ans =n
for i in range(n-1):
    for i  in range(i+1, n-1):
        for x, y in (inp[i], inp[j]):
            con[x][y]=0
            con[y][x]=0
        ans = min(ans,solve()) # 재귀
        for x, y in (inp[i],inp[j]):
            con[x][y]=1
            con[y][x]=1
print(ans)        

"""
9
1 3
3 2
3 5
4 6
6 5
6 8
8 7
7 9
=>
0
5
1 2
2 3
3 4
4 5
=>
1 
"""
        
        
        

    