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


def cmatrix():
    # Initialize empty screen with a more efficient data structure
    screen = {}
    for y in range(25):
        screen[y] = {}

    # Define character fall speeds with a focus on slower speeds
    speeds = {
        "slow": 0.3,
        "medium": 0.2,
        "fast": 0.1,
    }

    while True:
        # Add new characters with adjusted spawn rate
        for i in range(random.randint(1, 3)):  # Slightly reduced spawn rate
            column = random.randint(0, 79)
            color_choice = random.choice(list(COLORS.keys()))
            character = chr(random.randint(33, 126))
            fall_speed = random.choice(["slow", "slow", "slow", "medium", "fast"])  # Favor slower speeds
            screen[0][column] = f"{COLORS[color_choice]}{character}@{fall_speed}"

        # Shift characters down based on their individual speeds
        for y in range(24, 0, -1):
            for x in range(80):
                if screen[y-1].get(x) and screen[y-1][x].endswith("@"):
                    current_speed = float(screen[y-1][x].split("@")[-1])
                    if y + current_speed < 25:
                        screen[y][x] = screen[y-1][x][:-1] + "@" + str(current_speed)
                    else:
                        del screen[y][x]  # Efficiently remove characters at the bottom

        # Print the current screen with optimized output
        lines = [
            ''.join([char.split("@")[0] for char in screen.get(y, {}).values()])
            for y in range(25)
        ]
        print('\n'.join(lines))
        print("\033[0m")  # Reset color before new line
        sys.stdout.flush()

        # Increased delay for smoother perceived speed
        time.sleep(0.1)


if __name__ == "__main__":
    cmatrix()
