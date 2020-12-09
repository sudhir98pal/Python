# Q link->https://codeforces.com/contest/1450/problem/C1

t = int(input())
while t > 0:
    t = t-1
    n = int(input())
    a = []
    for i in range(0, n):
        s = []
        s[:0] = input()
        a.append(s)
    r = [0, 0, 0]
    for i in range(0, n):
        for j in range(0, n):
            x = (i+j) % 3
            if a[i][j] == 'X':
                r[x] += 1

    ans, index = n*n, 0

    for i in range(0, 3):
        if(r[i] < ans):
            ans, index = r[i], i
    for i in range(0, n):
        for j in range(0, n):
            if((i+j) % 3 == index and a[i][j] == 'X'):
                a[i][j] = 'O'
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j], end='')
        print()
