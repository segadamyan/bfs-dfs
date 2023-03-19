from collections import defaultdict


class Graph:
    def __init__(self):
        self.__graph = defaultdict(list)

    def add_edge(self, vertex_1: int, vertex_2: int) -> None:
        self.__graph[vertex_1].append(vertex_2)

    def bfs(self, vertex: int) -> list:
        queue = [vertex]
        visited = {vertex}
        result = []
        while queue:
            start = queue.pop(0)
            result.append(start)
            for i in self.__graph[start]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return result

    def dfs(self, node: int) -> list:
        result = []
        visited = {node}
        for child in self.__graph[node]:
            if child not in visited:
                self.__dfs_helper(node, visited, result)
        return result

    def __dfs_helper(self, vertex: int, visited: set, result: list) -> None:
        visited.add(vertex)
        result.append(vertex)
        for child in self.__graph[vertex]:
            if child not in visited:
                self.__dfs_helper(child, visited, result)
