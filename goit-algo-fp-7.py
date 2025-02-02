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


def main():
    num_rolls = 10000  # Кількість кидків (чим більше, тим точніше)

    results = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(results)

    print("Ймовірності сум двох кубиків (Monte Carlo):")
    for sum_val, prob in probabilities.items():
        print(f"Сума {sum_val}: {prob:.4f}")

    visualize_probabilities(probabilities)


if __name__ == "__main__":
    main()
