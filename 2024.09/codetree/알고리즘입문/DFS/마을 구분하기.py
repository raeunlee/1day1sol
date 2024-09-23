n = int(input())

l = []

for _ in range(n):
    row = list(map(int, input().split()))
    l.append(row)

visited = [[False] * n for i in range(n)]

d = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    global count
    visited[x][y] = True
    for each in d:
        nx = x + each[0]
        ny = y + each[1]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l[nx][ny] == 1:
            count += 1
            dfs(nx, ny)  

answer = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1 and not visited[i][j]:
            count = 1 # 카운트 선언
            dfs(i,j)
            answer.append(count)
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)

    
    


