from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def BFS(self, source, target):
        visited = [False] * (max(self.graph) + 1)

        queue = []
        queue.append(source)
        visited[source] = True
        while queue:

            s = queue.pop(0)
            if s == target:
                print(s)
                print("Found ", target)
                break
            print(s, end=" -> ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


print("Starting BFS")
g.BFS(0, 3)
