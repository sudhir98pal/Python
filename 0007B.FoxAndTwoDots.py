# B. Fox And Two Dots
# Q LINK https://codeforces.com/contest/510/problem/B


[n, m] = [int(x) for x in input().split()]
vis = [[False for i in range(55)] for i in range(0, 55)]


def isSafe(x, y) -> bool:
    return x >= 0 and x < n and y >= 0 and y < m


s = []
f = False
for i in range(0, n):
    _in = input()
    s.append(_in)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, px, py):
    vis[x][y] = True
    for i in range(0, 4):
        nx, ny = x+dx[i], y+dy[i]
        if(isSafe(nx, ny) and (s[x][y] == s[nx][ny]) and ((nx == px and ny == py) == False)):
            if(vis[nx][ny]):
                return True
            else:
                if dfs(nx, ny, x, y):
                    return True
    return False


for i in range(0, n):
    for j in range(0, m):
        if(vis[i][j] == False):
            if(dfs(i, j, -1, -1)):
                f = True
                break

if f:
    print('Yes')

else:
    print('No')
