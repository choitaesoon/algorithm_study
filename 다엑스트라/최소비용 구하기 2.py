import sys
from collections import defaultdict
import heapq
INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().rstrip().split())

dist = [INF] * (n+1) # 해당 노드까지 갔을 때의 최소비용(시작지점으로부터)
prev_node = [0] * (n+1)  # 특정 노드로 오기 직전의 노드를 저장하는 list

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0 # 시작 노드에 대해 0으로 초기화(비용이 0이므로)
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight:
            continue
        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                prev_node[adj_node] = node
                heapq.heappush(q, (cost, adj_node))

dijkstra(start)
print(dist[end])

path = [end] # 가장 마지막 노드부터 시작
now = end
while now != start: # 최단 경로를 역추적하는 과정, start까지 돌아가는 경로
    now = prev_node[now] # prev_node 즉, 해당 노드 직전 노드값을 저장
    path.append(now)

path.reverse()

print(len(path))
print(' '.join(map(str, path)))