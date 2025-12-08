# Basic timer built in game
import time
import pygame
time_front = pygame.font.Font('freesansbold.ttf', 32)

sec = 60
min = 0


def timer():
    print("Enter in min:")
    timer = int(input(":"))
    for i in range((timer)*60):
        time.sleep(1)
        sec -= 1
        if sec <= 0:
            min += 1
            sec = 60
        print(f"{(timer - 1) - min}:{sec}")
        time_display = time_front.render(
            f"Score: {0, 0}", True, (255, 255, 255))
        if sec > 10:
            zero = None
        if timer - min <= 0:
            break
