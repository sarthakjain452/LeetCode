import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]

        while pq:
            cost, node, count = heapq.heappop(pq)

            if node == n - 1:
                return cost

            if cost >= dist[node][count]:
                continue

            dist[node][count] = cost

            for nei, weight in graph[node]:

                if labels[node] == labels[nei]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    heapq.heappush(
                        pq, (new_cost, nei, new_count)
                    )

        return -1
