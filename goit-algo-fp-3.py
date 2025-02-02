import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]  # (distance, node)

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


def build_graph(edges):
    graph = {}
    for u, v, weight in edges:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = weight
    return graph


def visualize_graph(graph, shortest_paths, start_node):
    g = nx.DiGraph()
    pos = nx.spring_layout(g)  # або будь-який інший layout

    for u in graph:
        g.add_node(u)
        for v, weight in graph[u].items():
            g.add_edge(u, v, weight=weight)

    edge_labels = nx.get_edge_attributes(g, 'weight')

    nx.draw(g, pos, with_labels=True, node_size=700,
            node_color="skyblue", font_size=10, arrowsize=20)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    # Підсвічуємо найкоротші шляхи
    for end_node, distance in shortest_paths.items():
        if end_node != start_node and distance != float('inf'):
            path = find_path(g, start_node, end_node)
            if path:
                edges = list(zip(path, path[1:]))
                nx.draw_networkx_edges(
                    g, pos, edgelist=edges, edge_color='red', width=3, arrowsize=20)

    plt.show()


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


# Приклад використання:
edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'D', 5), ('B', 'E', 12),
    ('C', 'F', 10), ('C', 'G', 7),
    ('D', 'H', 3), ('E', 'H', 2),
    ('F', 'H', 5), ('G', 'H', 4)
]

graph = build_graph(edges)

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Найкоротші шляхи від вершини {start_node}: {shortest_paths}")

visualize_graph(graph, shortest_paths, start_node)
