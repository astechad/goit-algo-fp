import turtle
import math


def draw_pythagoras_tree(t, order, length):
    if order == 0:
        t.forward(length)
        t.backward(length)
        return

    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, order - 1, length / math.sqrt(2))
    t.right(90)
    draw_pythagoras_tree(t, order - 1, length / math.sqrt(2))
    t.left(45)
    t.backward(length)


def main():
    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    t = turtle.Turtle()
    t.speed(0)

    recursion_level = int(screen.textinput(
        "Рівень рекурсії", "Введіть рівень рекурсії (ціле число):"))

    t.up()
    t.goto(0, -200)
    t.down()
    t.left(90)

    draw_pythagoras_tree(t, recursion_level, 100)

    screen.mainloop()


if __name__ == "__main__":
    main()
