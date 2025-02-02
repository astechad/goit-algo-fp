items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(
    ), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)
    selected_items = []
    total_cost = 0

    for item_name, item_data in sorted_items:
        if total_cost + item_data["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_data["cost"]

    return selected_items


def dynamic_programming(items, budget):
    n = len(items)
    # Створюємо матрицю для зберігання максимальної калорійності для кожного підмножини страв та бюджету
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо матрицю згідно з алгоритмом динамічного програмування
    for i in range(1, n + 1):
        item_name = list(items.keys())[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]
        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(calories + dp[i - 1][j - cost], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # Відновлюємо оптимальний набір страв
    selected_items = []
    i = n
    j = budget
    while i > 0 and j > 0:
        item_name = list(items.keys())[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(item_name)
            j -= cost
        i -= 1

    return selected_items


# Приклад використання
budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:", greedy_result)

dynamic_result = dynamic_programming(items, budget)
print("Динамічне програмування:", dynamic_result)
