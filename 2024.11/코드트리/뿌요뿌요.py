import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

visited = [[False] * n for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, num):
    global count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == num:
            visited[nx][ny] = True
            count += 1
            dfs(nx, ny, num)

count_list = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            count = 1
            visited[i][j] = True
            dfs(i, j, graph[i][j])
            count_list.append(count)
            
count_list.sort()
bomb = 0
for c in count_list:
    if c >= 4:
        bomb+=1
print(bomb, count_list[-1])


    
