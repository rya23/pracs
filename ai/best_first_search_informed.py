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

# g.addEdge(0, 2, 6)
# g.addEdge(0, 1, 3)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 4, 9)
# g.addEdge(1, 5, 8)
# g.addEdge(2, 6, 12)
# g.addEdge(2, 7, 14)
# g.addEdge(3, 8, 7)
# g.addEdge(8, 9, 5)
# g.addEdge(8, 10, 6)
# g.addEdge(9, 11, 1)
# g.addEdge(9, 12, 10)
# g.addEdge(9, 13, 2)

# source = 0
# target = 9


g.addEdge(1, 2, 4)  # Edge from node 1 to node 2 with cost 4
g.addEdge(1, 3, 6)  # Edge from node 1 to node 3 with cost 6
g.addEdge(3, 4, 8)  # Edge from node 3 to node 4 with cost 8
g.addEdge(2, 4, 7)  # Edge from node 2 to node 4 with cost 7
g.addEdge(4, 2, 5)  # Edge from node 4 to node 2 with cost 5
g.addEdge(2, 5, 3)  # Edge from node 2 to node 5 with cost 3
g.addEdge(5, 4, 9)  # Edge from node 5 to node 4 with cost 9

source = 1
target = 5
g.bestFirstSearch(source, target)
