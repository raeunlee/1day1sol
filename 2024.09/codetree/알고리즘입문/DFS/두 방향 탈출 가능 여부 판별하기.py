n, m = map(int, input().split())

l = []
for i in range(n):
    row = list(map(int, input().split()))
    l.append(row)

visited = [[0 for _ in range(m)] for _ in range(n)]

dir = [(0, 1), (1, 0)]

def dfs(x, y):
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m:  # 인덱스가 유효한지 먼저 확인
            if l[nx][ny] == 1 and not visited[nx][ny]:  # 이후에 방문 및 값 체크
                visited[nx][ny] = 1
                dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)
print(visited[n - 1][m - 1])
