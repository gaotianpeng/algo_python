from typing import List, Optional, Generator, IO
from collections import deque

class Graph(object):
    def __init__(self, vertex_num: int):
        self.v_num = vertex_num
        self.adj_tbl = [[] for _ in range(vertex_num)]

    def print_all(self):
        print(self.adj_tbl)

    def add_edge(self, s: int, t: int) -> None:
        if s > self.v_num or t > self.v_num:
            return False
        self.adj_tbl[s].append(t)
        self.adj_tbl[t].append(s)
        return True

    def _gen_path(self, s: int, t: int, prev: List[Optional[int]]) -> Generator[str, None, None]:
        if prev[t] or s != t:
            yield from self._gen_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s:int, t:int) -> IO[str]:
        if s == t:
            return
        visited = [False] * self.v_num
        visited[s] = True
        q = deque()
        q.append(s)
        prev = [None] * self.v_num

        while q:
            v = q.popleft()
            for neighbour in self.adj_tbl[v]:
                if not visited[neighbour]:
                    prev[neighbour] = v
                    if neighbour == t:
                        print("->".join(self._gen_path(s, t, prev)))
                        return
                    visited[neighbour] = True
                    q.append(neighbour)

    def dfs(self, s: int, t: int) -> IO[str]:
        found = False
        visited = [False] * self.v_num
        prev = [None] * self.v_num
        def _dfs(from_vertex: int) -> None:
            nonlocal found
            if found: return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbour in self.adj_tbl[from_vertex]:
                if not visited[neighbour]:
                    prev[neighbour] = from_vertex
                    _dfs(neighbour)

        _dfs(s)
        print("->".join(self._gen_path(s, t, prev)))

if __name__ == '__main__':
    print('__main__')
    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    print(graph)
    graph.print_all()
    graph.bfs(0, 4)
    graph.dfs(0, 4)
