# 백트래킹, 모든경우의수 확인 브루트포스 
# 동서남북 움직이고, 합쳐졌으면 두번은 다시못합친다
# N-1 칸부터 0번째 칸까지 움직일수 있다
# 0022 ->0004
# 동쪽끝 계산 -1 씩 마지노선 블록을 움직인다
# 서쪽으로 움직인다.. 동쪽 움직이기전 게임판  서쪽으로 움직여야 함

from copy import deepcopy
graph= []
for i in range(n):
    graph.append(list(map(int,input().split())))
    
def move(board,dir):
    if dir == 0 : # 동쪽
        for i in range(n):
            top = n-1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    tmp =board[i][j]
                    board[i][j] =0
                    # TMP = 블록위치
                    if board[i][top] ==0:
                        board[i][top] =tmp
                    # 같으면 계산
                    elif board[i][top] == tmp:
                        board[i][top] = tmp*2
                        top -=1
                    # 다르면 마지노선 줄인다
                    else:
                        top -=1
                        board[i][top] =tmp
    elif dir ==1 : # 서쪽
        for i in range(n):
            top = 0
            for j in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] =0
                    if board[i][top] ==0:
                        board[i][top]== tmp
                    elif board[i][top] ==tmp:
                        board[i][top] == tmp*2
                        top+=1
                    else:
                        top +=1
                        board[i][top] = tmp
    elif dir ==2 : # 남쪽
        for j in range(n):
            top = n-1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] =0
                    if board[top][j] ==0:
                        board[top][j]== tmp
                    elif board[top][j] ==tmp:
                        board[top][j] == tmp*2
                        top -=1
                    else:
                        top -=1
                        board[top][j] = tmp
    else: #북
        for j in range(n):
            top = 0
            for i in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j]=0
                    if board[top][j] ==0:
                        board[top][0] == tmp
                    elif board[top][j] ==tmp:
                        board[top][j]= tmp *2
                        top +=1
                    else:
                        top +=1
                        board[top][j] =tmp
    return board

def dfs(board,cnt):
    global ans 
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return
    for i in range(4):
        tmp_board = move(deepcopy(board),i)
        dfs(tmp_board,cnt+1)
ans = 0
dfs(graph,0)
print(ans)
                
                    
            