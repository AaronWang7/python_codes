import time
sec = 60
min = 0
print("Enter in min:")
timer = int(input(":"))
for i in range((timer)*60):
    time.sleep(1)
    sec -= 1
    if sec <= 0:
        min += 1
        sec = 60
    print(f"{(timer - 1) - min}:{sec}")
    if sec > 10:
        zero = None
    if timer - min <= 0:
        break
