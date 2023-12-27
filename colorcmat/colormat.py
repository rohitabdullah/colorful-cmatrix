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
    # Initialize empty screen
    screen = [[' ' for _ in range(80)] for _ in range(25)]

    # Define character fall speeds
    speeds = {
        "slow": 0.3,
        "medium": 0.2,
        "fast": 0.1,
    }

    while True:
        # Add new characters with varying spawn rate and speed
        for i in range(random.randint(2, 4)):
            column = random.randint(0, 79)
            color_choice = random.choice(list(COLORS.keys()))
            character = chr(random.randint(33, 126))
            fall_speed = random.choice(list(speeds.keys()))
            screen[0][column] = f"{COLORS[color_choice]}{character}@{fall_speed}"

        # Shift characters down based on their individual speeds
        for y in range(24, 0, -1):
            for x in range(80):
                if screen[y-1][x].endswith("@"):
                    # Extract speed from character string
                    current_speed = float(screen[y-1][x].split("@")[-1])
                    if y + current_speed < 25:
                        screen[y][x] = screen[y-1][x][:-1] + "@" + str(current_speed)
                    else:
                        screen[y][x] = " "
                else:
                    screen[y][x] = screen[y-1][x]

        # Print the current screen with color reset
        for line in screen:
            print(''.join([char.split("@")[0] for char in line]), end='')
        print("\033[0m")  # Reset color before new line

        # Clear the output buffer
        sys.stdout.flush()

        # Adjust delay for natural flow
        time.sleep(0.05)


if __name__ == "__main__":
    cmatrix()
