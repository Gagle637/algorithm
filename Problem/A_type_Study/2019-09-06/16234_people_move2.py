import sys; sys.stdin = open('16234.txt', 'r')
from collections import deque

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def BFS(v):
    global c, check, total
    Q = deque()
    Q.append(v)
    check.append(v)
    visit[v[0]][v[1]] = True
    c += 1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N :
                if visit[tx][ty] == False:
                    if L <= abs(people[tx][ty] - people[x][y]) <= R:
                        Q.append([tx, ty])
                        visit[tx][ty] = True
                        check.append([tx,ty])
                        c += 1
        # print(Q)


N, L, R = list(map(int, input().split()))
people = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    country = []
    visit = [[False for _ in range(N)] for __ in range(N)]
    for x in range(N):
        for y in range(N):
            if visit[x][y]: continue
            check = []
            c = 0
            BFS([x, y])
            if c > 1:
                country.append(check)
        # print(check)
    if country:
        for i in range(len(country)):
            total = 0
            for j in country[i]:
                x, y = j
                total += people[x][y]
            total = total//len(country[i])
            for j in country[i]:
                x,  y = j
                people[x][y] = total
    else:
        break
    # for i in range(N):
    #     print(people[i])
    # print()
    result += 1
print(result)


