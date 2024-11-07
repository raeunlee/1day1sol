import heapq

# 1번 마을에서 N개의 마을 중에서 K시간 이하로 배달이 가능한 마을
def dijkstra(dist, maps):
    h = []
    # 현재노드, cost
    heapq.heappush(h, [1, 0]) 
    while h:
        node, cost = heapq.heappop(h)
        for n, c in maps[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(h, [n,  c + cost]) # 다음노드, count append

def solution(N, road, K):
    answer = 0
    
    dist = [1e9 for i in range(N+1)]
    dist[1] = 0
    
    maps = [[] for i in range(N+1)]
    
    # a,b 연결된 두 마을의 번호 / c 둘 사이 거리이다
    for r in road:
        a, b, c = r
        maps[a].append((b,c))
        maps[b].append((a,c))
    
    #print(maps)
    
    dijkstra(dist, maps)

    for i in range(len(dist)):
        if dist[i] <= K:
            answer += 1
    return answer
