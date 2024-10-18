from collections import defaultdict
from queue import PriorityQueue


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, cost):
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    def bestFirstSearch(self, source, target):

        visited = [False] * (max(self.graph) + 1)

        pq = PriorityQueue()

        pq.put((0, source))
        visited[source] = True

        while pq.empty() == False:
            u = pq.get()[1]
            print(u, end=" -> ")

            if u == target:
                break

            for v, c in self.graph[u]:
                if visited[v] == False:
                    visited[v] = True
                    pq.put((c, v))
        print()


g = Graph()

g.addEdge(0, 2, 6)
g.addEdge(0, 1, 3)
g.addEdge(0, 3, 5)
g.addEdge(1, 4, 9)
g.addEdge(1, 5, 8)
g.addEdge(2, 6, 12)
g.addEdge(2, 7, 14)
g.addEdge(3, 8, 7)
g.addEdge(8, 9, 5)
g.addEdge(8, 10, 6)
g.addEdge(9, 11, 1)
g.addEdge(9, 12, 10)
g.addEdge(9, 13, 2)

source = 0
target = 9
g.bestFirstSearch(source, target)
