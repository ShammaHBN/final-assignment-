import networkx as nx
import matplotlib.pyplot as plt

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

    def delete_road(self, source, destination):
        if source in self.vertices and destination in self.vertices[source]:
            del self.vertices[source][destination]
            del self.vertices[destination][source]

    def get_roads_at_intersection(self, intersection):
        return self.vertices.get(intersection, {})

# Test Cases
graph = Graph()
graph.add_road(1, 2, 101, 'Main Street', 5)
graph.add_road(1, 3, 102, 'Broadway', 7)
graph.add_road(2, 3, 103, 'Elm Street', 4)
graph.add_road(2, 4, 104, 'Maple Avenue', 6)
graph.add_road(3, 4, 105, 'Cedar Lane', 3)

G = nx.Graph()

# Add edges
for source, edges in graph.vertices.items():
    for destination, data in edges.items():
        G.add_edge(source, destination, road_name=data['road_name'], length=data['length'])

# Draw graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", font_color="black")
edge_labels = nx.get_edge_attributes(G, 'road_name')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

plt.title("Road Network")
plt.show()


