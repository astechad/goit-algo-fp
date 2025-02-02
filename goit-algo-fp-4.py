import uuid
import networkx as nx
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]
    for i in range(len(nodes) // 2 - 1, -1, -1):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2
        if left_child_index < len(nodes):
            nodes[i].left = nodes[left_child_index]
        if right_child_index < len(nodes):
            nodes[i].right = nodes[right_child_index]
    return nodes[0]


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


def draw_heap(heap):
    try:
        import matplotlib.pyplot as plt
        import numpy as np  # Імпортуємо numpy тут
    except KeyboardInterrupt:
        print("Імпорт matplotlib або numpy перервано користувачем.")
        return
    except ImportError as e:
        print(f"Помилка імпорту: {
              e}. Перевірте, чи встановлені matplotlib та numpy.")
        return

    root = build_heap_tree(heap)
    if not root:
        print("Купа порожня")
        return

    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, with_labels=True)
    plt.show()


# Приклад використання
heap = [1, 3, 6, 5, 9, 8]
draw_heap(heap)  # Викликаємо draw_heap, а не draw_tree
