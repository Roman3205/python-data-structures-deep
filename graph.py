import heapq
from collections import deque

class Graph:
    def __init__(self, directed = False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""

        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"

        return graph_str

    # O(1)
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists")

    # O(1) or O(n)
    def remove_node(self, node):
        if node not in self.adj_list:
            raise ValueError("Node already exists")

        for neighbors in self.adj_list.values():
            neighbors.discard(node)

        del self.adj_list[node]

    # O(1)
    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_list[to_node].add((from_node, weight))

    # O(1)
    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exist")
            
            if not self.directed:
                if from_node in self.adj_list[to_node]:
                    self.adj_list[to_node].remove(from_node)
        else:
            raise ValueError("Edge does not exist")

    # O(1)
    def get_neighbors(self, node):
        return self.adj_list.get(node, set())

    # O(1)
    def has_node(self, node):
        return node in self.adj_list

    # O(1)
    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False

    # O(n)
    def get_nodes(self):
        return list(self.adj_list.keys())

    # O(v+e) where v is number of vertices and e is number of edges
    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_node, to_node))
        return edges

    # O(v + e) where v is number of vertices and e is number of edges
    def bfs(self, start):
        visited = set()
        queue = deque([start]) # O (v^2 + e) if we use list instead of deque
        order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor in self.get_neighbors(node):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order

    # O(v + e) where v is number of vertices and e is number of edges
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        for neighbor in self.get_neighbors(start):
            if isinstance(neighbor, tuple):
                neighbor = neighbor[0]
            if neighbor not in visited:
                self.dfs(neighbor, visited)

        return visited
    
    # O((v + e) log v) where v is number of vertices and e is number of edges
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.get_neighbors(current_node):
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = current_distance + weight

                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(priority_queue, (distance, to))
        return distances

    # O((v + e) log v) where v is number of vertices and e is number of edges
    def shortest_path(self, start, end):
        distances = {node: float('inf') for node in self.adj_list}
        distances[start] = 0

        previous_nodes = {node: None for node in self.adj_list}

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.get_neighbors(current_node):
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = current_distance + weight

                if distance < distances[to]:
                    distances[to] = distance
                    previous_nodes[to] = current_node
                    heapq.heappush(priority_queue, (distance, to))
        print('-------')
        print(distances, previous_nodes)
        print('-------')
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        
        path.reverse()
        if path[0] == start:
            return path
        return []

    
if __name__ == '__main__':
    graph = Graph()
    graph.add_edge('A', 'C', 5)
    graph.add_edge('A', 'B', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('D', 'C', 5)
    graph.add_edge('C', 'E', 6)


    print(graph)

    print(graph.bfs('A'))
    print(graph.dfs('A'))
    print(graph.dijkstra('A'))
    print(graph.shortest_path('A', 'C'))