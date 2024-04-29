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

    def get_roads_at_intersection(self, intersection):
        return self.vertices.get(intersection, {})

# Test Cases
graph = Graph()
graph.add_road(1, 2, 101, 'Main Street', 5)
graph.add_road(1, 3, 102, 'Broadway', 7)
graph.add_road(2, 3, 103, 'Elm Street', 4)
graph.add_road(2, 4, 104, 'Maple Avenue', 6)
graph.add_road(3, 4, 105, 'Cedar Lane', 3)

for intersection, roads in graph.vertices.items():
    print("Roads at intersection", intersection, ":", roads)
