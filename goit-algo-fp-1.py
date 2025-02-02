class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    dummy = Node(0)  # Фіктивний вузол для спрощення вставки
    dummy.next = head
    sorted_head = dummy

    curr = head
    while curr:
        prev = sorted_head
        while prev.next and prev.next.data < curr.data:
            prev = prev.next

        if prev.next != curr:  # Потрібна вставка
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = next_node
        else:
            curr = curr.next  # елемент вже на своєму місці

    return sorted_head.next


def merge_sorted_linked_lists(head1, head2):
    dummy = Node(0)
    curr = dummy

    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    # Додаємо залишки одного зі списків (якщо вони є)
    curr.next = head1 or head2

    return dummy.next

# Приклад використання:


# Створення списку
head = Node(5)
head.next = Node(2)
head.next.next = Node(8)
head.next.next.next = Node(1)

# Реверсування списку
reversed_head = reverse_linked_list(head)

# Вивід списку


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


print("Реверсований список:")
print_list(reversed_head)

# Створення іншого списку
head2 = Node(3)
head2.next = Node(6)
head2.next.next = Node(9)
head2.next.next.next = Node(10)


# Сортування списку
sorted_head = insertion_sort_linked_list(reversed_head)
print("Відсортований список:")
print_list(sorted_head)

# Створення ще одного списку
head3 = Node(4)
head3.next = Node(7)

# Злиття двох відсортованих списків
merged_head = merge_sorted_linked_lists(sorted_head, head3)
print("Злитий та відсортований список:")
print_list(merged_head)
