import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        results.append(roll1 + roll2)
    return results


def calculate_probabilities(results):
    counts = {}
    for sum_val in results:
        counts[sum_val] = counts.get(sum_val, 0) + 1

    probabilities = {}
    for sum_val, count in counts.items():
        probabilities[sum_val] = count / len(results)
    return probabilities


def visualize_probabilities(probabilities):
    sums = sorted(probabilities.keys())
    probs = [probabilities[s] for s in sums]

    plt.bar(sums, probs)
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірності сум двох кубиків (Monte Carlo)")
    plt.xticks(sums)
    plt.show()


def calculate_analytical_probabilities():
    # Аналітичні ймовірності для сум двох кубиків
    analytical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    return analytical_probs


def compare_probabilities(monte_carlo_probs, analytical_probs):
    comparison = {}
    for sum_val in sorted(monte_carlo_probs.keys()):
        mc_prob = monte_carlo_probs[sum_val]
        analytical_prob = analytical_probs[sum_val]
        difference = abs(mc_prob - analytical_prob)
        comparison[sum_val] = difference
    return comparison


def main():
    num_rolls = 10000  # Кількість кидків (чим більше, тим точніше)

    results = simulate_dice_rolls(num_rolls)
    monte_carlo_probs = calculate_probabilities(results)
    analytical_probs = calculate_analytical_probabilities()

    print("Ймовірності сум двох кубиків (Monte Carlo):")
    for sum_val, prob in monte_carlo_probs.items():
        print(f"Сума {sum_val}: {prob:.4f}")

    visualize_probabilities(monte_carlo_probs)

    comparison = compare_probabilities(monte_carlo_probs, analytical_probs)
    print("\nПорівняння з аналітичними значеннями:")
    for sum_val, diff in comparison.items():
        print(f"Сума {sum_val}: Різниця {diff:.4f}")

    # Виводимо середню різницю для оцінки точності Monte Carlo
    average_difference = sum(comparison.values()) / len(comparison)
    print(f"\nСередня різниця: {average_difference:.4f}")

    # Записуємо висновки у файл README.md
    with open("README.md", "w") as f:
        f.write("# Результати моделювання кидання двох кубиків методом Монте-Карло\n\n")
        f.write("## Опис\n")
        f.write("Цей код моделює кидання двох кубиків задану кількість разів та обчислює ймовірності сум, використовуючи метод Монте-Карло. ")
        f.write("Результати порівнюються з аналітично обчисленими ймовірностями.\n\n")
        f.write("## Результати\n")
        f.write("Отримані ймовірності сум (Monte Carlo):\n")
        for sum_val, prob in monte_carlo_probs.items():
            f.write(f"- Сума {sum_val}: {prob:.4f}\n")
        f.write("\nПорівняння з аналітичними значеннями:\n")
        for sum_val, diff in comparison.items():
            f.write(f"- Сума {sum_val}: Різниця {diff:.4f}\n")
        f.write(f"\nСередня різниця: {average_difference:.4f}\n\n")
        f.write("## Висновки\n")
        f.write(f"Отримана середня різниця між результатами моделювання та аналітичними значеннями становить {
                average_difference:.4f}. ")
        f.write("Це свідчить про те, що метод Монте-Карло дає досить точні результати, особливо зі збільшенням кількості кидків.")
        f.write(
            "Згенеровані методом Монте-Карло ймовірності наближаються до теоретичних значень.")


if __name__ == "__main__":
    main()
