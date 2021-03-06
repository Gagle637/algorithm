def DFS(x, y):
    global maze, result
    visit[x][y] =True
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx <= n-1 and 0<= ty <=n-1:
            if maze[tx][ty] == 0 and visit[tx][ty] == False:
                DFS(tx, ty)
            if maze[tx][ty] == 3:
                result = 1

import sys; sys.stdin = open('4613.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    visit = [[False for _ in range(n)] for __ in range(n)]
    maze = [list(map(int, list(input()))) for i in range(n)]
    for x in range(len(maze)):
        if maze[x].count(2):
            DFS(x, maze[x].index(2))
            break
    print('#{} {}'.format(tc, result))



# import sys ; sys.stdin = open('4613.txt', 'r')
# def DFS(x,y):
#     global result
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     visit[x][y] = True
#     # print(x,y)
#     for i in range(4):
#         tx = x +dx[i]
#         ty = y +dy[i]
#         if 0 <= tx < N and 0 <= ty <N:
#             if arr[tx][ty] == 0 and visit[tx][ty] == False:
#                 DFS(tx,ty)
#             if arr[tx][ty] == 2:
#                 result = 1
#                 return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     result = 0
#     arr = [list(map(int, input())) for _ in range(N)]
#     visit =[[False for _ in range(N)] for _ in range(N)]
#     for x in range(N):
#         for y in range(N):
#             if arr[x][y]==3:
#                 DFS(x, y)
#                 break
#     print(result)
