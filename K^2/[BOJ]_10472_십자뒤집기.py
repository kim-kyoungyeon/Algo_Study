# dfs 문제
# bfs,set 
# x번째 칸을 누르면 뒤집히는 칸들의 번호
import sys 
import copy
from collections import deque
# 원래, 우 ,좌 상,하
dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]

def convert_board(board,x,y):
    # deepcopy= 원형리스트 내부객체까지 다  변경
    ret= copy.deepcopy(board)
    
    for i in range(5):
        nx, ny =x +dx[i]+dy[i]
        if 0 <= nx < 3 and 0 <=ny <3 :
            ret[nx][ny] = '*' if ret[nx][ny]=='.' else '.'
    return ret

    # 중복상태 순회 피하기
    # 보드가검은색 =1 아닐경우 0
    # 이진수로 중복 검증
def convert_to_binary(board):
    binary_str=''

    for x in range(3):
        for y in range(3):
            binary_str +='0' if board[x][y] =='.' else '1'
    return int(binary_str,2)


def bfs(goal):
    time =0
    init_board=[['.'] * 3 for _ in range(3)]
    visit=[0]*1000
    
    q = deque([init_board])
    visit[convert_to_binary(init_board)] =1
    
    while q:
        loop=len(q)
        for _ in range(loop):
            board = q.popleft()
            if board == goal:
                return time
            
            for row in range(3):
                for col in range(3):
                    next_board = convert_board(board,row,col)
                    binary_code = convert_to_binary(next_board)
                    
                    if not visit[binary_code]:
                        q.append(next_board)
                        visit[binary_code]=1
                    
        time +=1
        
def solution(testcase):
    time=bfs(testcase)
    
    return time


if __name__== '__main__':
    T= int(input())
    for _ in range(T):
        testcase= [list(sys.stdin.readline().strip()) for _ in range(3)]
        answer = solution(testcase)
        print(answer)
                
        