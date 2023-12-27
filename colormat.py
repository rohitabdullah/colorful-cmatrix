import random
import time
import sys

COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
}


def generate_gradient_color():
    # Implement your preferred gradient color generation logic here
    # You can use external libraries or custom algorithms
    return random.choice(list(COLORS.values()))  # Replace with actual gradient code


def cmatrix():
    screen = {}
    for y in range(25):
        screen[y] = {}

    speeds = {
        "slow": 0.3,
        "medium": 0.2,
        "fast": 0.1,
    }

    while True:
        for i in range(random.randint(1, 3)):
            column = random.randint(0, 79)
            color = generate_gradient_color()
            character = chr(random.randint(33, 126))
            fall_speed = random.choice(["slow", "slow", "slow", "medium", "fast"])
            screen[0][column] = f"{color}{character}@{fall_speed}"

        for y in range(24, 0, -1):
            for x in range(80):
                if screen[y - 1].get(x) and screen[y - 1][x].endswith("@"):
                    current_speed = float(screen[y - 1][x].split("@")[-1])
                    if y + current_speed < 25:
                        screen[y][x] = screen[y - 1][x][:-1] + "@" + str(current_speed)
                    else:
                        del screen[y][x]

        lines = [
            ''.join([char.split("@")[0] for char in screen.get(y, {}).values()])
            for y in range(25)
        ]
        print('\n'.join(lines))
        print("\033[0m")  # Reset color before new line
        sys.stdout.flush()

        time.sleep(0.1)


if __name__ == "__main__":
    cmatrix()
