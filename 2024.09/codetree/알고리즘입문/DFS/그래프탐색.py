n,m = map(int, input().split())

l = []
for i in range(n+1):
    l.append([])

for i in range(m):
    x, y = map(int, input().split())
    l[x].append(y)
    l[y].append(x)

#print(l)
# 1에서 시작해서 도달할 수 있는 정점의 수

visited = [False for i in range(n+1)]
count = 0

def dfs(vertex):
    global count
    for curr_v in l[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            count += 1
            dfs(curr_v)

visited[1] = True            
dfs(1)
print(count)
