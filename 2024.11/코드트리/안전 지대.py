import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
arr = []

max_num = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    max_num = max(max_num, max(tmp))
    arr.append(tmp)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,k):
    global arr
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] > k and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, k)

count_list = []
for num in range(1, max_num + 1):
    count = 0 
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > num and not visited[i][j]:
                visited[i][j] = True
                dfs(i,j,num)
                count += 1
    count_list.append([num, count])

ans = sorted(count_list, key = lambda x : -x[1])
print(ans[0][0], ans[0][1])

