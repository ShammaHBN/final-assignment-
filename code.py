# -*- coding: utf-8 -*-
"""Code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1951qjUcFe3VGFljRKpCJWo6KF-Iv6jv1
"""

import heapq

class Post:
    def __init__(self, datetime, post, person, views):
        self.datetime = datetime
        self.post = post
        self.person = person
        self.views = views

class SocialMediaSystem:
    def __init__(self):
        self.posts = {}
        self.bst_root = None
        self.max_heap = []

    # Hash Table Operations
    def add_post(self, post):
        self.posts[post.datetime] = post
        # Update Binary Search Tree
        self._insert_bst(post)
        # Update Max Heap
        self._insert_heap(post)

    def find_post(self, datetime):
        return self.posts.get(datetime, None)

    # Binary Search Tree Operations
    def _insert_bst(self, post):
        if not self.bst_root:
            self.bst_root = Node(post)
        else:
            self.bst_root.insert(post)

    def find_range(self, start, end):
        return self.bst_root.find_range(start, end) if self.bst_root else []

    # Heap Operations
    def _insert_heap(self, post):
        heapq.heappush(self.max_heap, (-post.views, post))

    def get_most_viewed_post(self):
        return heapq.heappop(self.max_heap)[1] if self.max_heap else None

class Node:
    def __init__(self, post):
        self.post = post
        self.left = None
        self.right = None

    def insert(self, post):
        if post.datetime < self.post.datetime:
            if not self.left:
                self.left = Node(post)
            else:
                self.left.insert(post)
        else:
            if not self.right:
                self.right = Node(post)
            else:
                self.right.insert(post)

    def find_range(self, start, end):
        posts = []
        if start <= self.post.datetime <= end:
            posts.append(self.post)
        if self.left and start <= self.left.post.datetime:
            posts.extend(self.left.find_range(start, end))
        if self.right and end >= self.right.post.datetime:
            posts.extend(self.right.find_range(start, end))
        return posts

# Test cases for Hash Table
def test_hash_table():
    system = SocialMediaSystem()
    post1 = Post("2024-04-28 10:00:00", "Hello World!", "User1", 100)
    post2 = Post("2024-04-28 12:00:00", "Goodbye World!", "User2", 200)
    system.add_post(post1)
    system.add_post(post2)

    assert system.find_post("2024-04-28 10:00:00") == post1
    assert system.find_post("2024-04-28 12:00:00") == post2
    assert system.find_post("2024-04-28 08:00:00") is None

# Test cases for Binary Search Tree
def test_binary_search_tree():
    system = SocialMediaSystem()
    post1 = Post("2024-04-28 10:00:00", "Hello World!", "User1", 100)
    post2 = Post("2024-04-28 12:00:00", "Goodbye World!", "User2", 200)
    system.add_post(post1)
    system.add_post(post2)

    posts_in_range = system.find_range("2024-04-28 09:00:00", "2024-04-28 13:00:00")
    assert len(posts_in_range) == 2
    assert post1 in posts_in_range
    assert post2 in posts_in_range

# Test cases for Heap
def test_heap():
    system = SocialMediaSystem()
    post1 = Post("2024-04-28 10:00:00", "Hello World!", "User1", 100)
    post2 = Post("2024-04-28 12:00:00", "Goodbye World!", "User2", 200)
    system.add_post(post1)
    system.add_post(post2)

    most_viewed_post = system.get_most_viewed_post()
    assert most_viewed_post == post2

if __name__ == "__main__":
    test_hash_table()
    test_binary_search_tree()
    test_heap()
    print("All test cases passed.")

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

    def add_house(self, house_id, intersection):
        self.add_vertex(house_id)
        self.vertices[house_id]['intersection'] = intersection

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
                print(edge)
                try:
                   weight = edge['length']
                except:
                  continue
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
def test_graph_representation():
    graph = Graph()
    graph.add_road(1, 2, 101, 'Main Street', 5)
    graph.add_road(1, 3, 102, 'Broadway', 7)
    graph.add_road(2, 3, 103, 'Elm Street', 4)

    print("Roads at intersection 1:", graph.get_roads_at_intersection(1))
    print("Roads at intersection 2:", graph.get_roads_at_intersection(2))
    print("Roads at intersection 3:", graph.get_roads_at_intersection(3))

def test_package_distribution():
    graph = Graph()
    graph.add_road(1, 2, 101, 'Main Street', 5)
    graph.add_road(1, 3, 102, 'Broadway', 7)
    graph.add_road(2, 3, 103, 'Elm Street', 4)
    graph.add_house(201, 3)

    print("Shortest path from intersection 1 to house 201:", graph.dijkstra_shortest_path(1, 201))

def test_shortest_distance():
    graph = Graph()
    graph.add_road(1, 2, 101, 'Main Street', 5)
    graph.add_road(1, 3, 102, 'Broadway', 7)
    graph.add_road(2, 3, 103, 'Elm Street', 4)

    print("Shortest distance between intersection 1 and intersection 3:", graph.dijkstra_shortest_path(1, 3))

# Run test cases
test_graph_representation()
test_package_distribution()
test_shortest_distance()