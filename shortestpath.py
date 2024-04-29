class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = {}

    def add_road(self, source, destination, road_id, road_name, length):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.vertices[source][destination] = {'road_id': road_id, 'road_name': road_name, 'length': length}
        self.vertices[destination][source] = {'road_id': road_id, 'road_name': road_name, 'length': length}

    def dijkstra_shortest_path(self, start, end):
        visited = set()
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        previous_vertices = {}

        while len(visited) < len(self.vertices):
            current_vertex = min(
                (vertex, distance) for vertex, distance in distances.items() if vertex not in visited
            )[0]
            visited.add(current_vertex)
            for neighbor, edge in self.vertices[current_vertex].items():
                weight = edge['length']
                distance = distances[current_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex

        path, current_vertex = [], end
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices.get(current_vertex, None)
        return path, distances[end]

# Test Cases
graph = Graph()
graph.add_road(1, 2, 101, 'Main Street', 5)
graph.add_road(1, 3, 102, 'Broadway', 7)
graph.add_road(2, 3, 103, 'Elm Street', 4)
graph.add_road(2, 4, 104, 'Maple Avenue', 6)
graph.add_road(3, 4, 105, 'Cedar Lane', 3)

print(graph.dijkstra_shortest_path(1, 3))
