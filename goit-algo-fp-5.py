import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors={}, title="Binary Tree"):
    try:
        import matplotlib.pyplot as plt  # Імпорт тут
        import networkx as nx  # Імпорт тут
    except ImportError as e:
        print(f"Помилка імпорту: {
              e}. Перевірте, чи встановлені matplotlib та networkx.")
        return

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    default_color = "skyblue"
    node_colors = [colors.get(node, default_color) for node in tree.nodes()]
    labels = {node: tree.nodes[node]['label'] for node in tree.nodes()}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=node_colors, with_labels=True)
    plt.title(title)
    plt.show()


def dfs(root):
    if not root:  # Перевірка на None
        return

    visited = {}
    stack = [(root, 0)]
    color_counter = 0

    while stack:
        node, color_intensity = stack.pop()
        if node and node.id not in visited:  # Перевірка на None та відвіданість
            color = get_color(color_intensity)
            visited[node.id] = color
            draw_tree(root, visited, title=f"DFS: {node.val}")

            if node.right:
                stack.append((node.right, color_intensity + 1))
            if node.left:
                stack.append((node.left, color_intensity + 1))


def bfs(root):
    if not root:  # Перевірка на None
        return

    visited = {}
    queue = deque([(root, 0)])
    color_counter = 0

    while queue:
        node, color_intensity = queue.popleft()
        if node and node.id not in visited:  # Перевірка на None та відвіданість
            color = get_color(color_intensity)
            visited[node.id] = color
            draw_tree(root, visited, title=f"BFS: {node.val}")

            if node.left:
                queue.append((node.left, color_intensity + 1))
            if node.right:
                queue.append((node.right, color_intensity + 1))


def get_color(intensity):
    base_color = 0x1296F0  # Example base color
    max_intensity = 10  # Adjust as needed

    r = (base_color >> 16) & 0xFF
    g = (base_color >> 8) & 0xFF
    b = base_color & 0xFF

    intensity_factor = 0.5 + 0.5 * (max_intensity - intensity) / max_intensity
    r = int(r * intensity_factor)
    g = int(g * intensity_factor)
    b = int(b * intensity_factor)

    return f"#{r:02X}{g:02X}{b:02X}"


# Створення дерева (приклад)
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
