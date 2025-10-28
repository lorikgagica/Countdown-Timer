# Countdown Timer

import time

# Step 1: Get user input for countdown start
start = int(input("Enter the number to start the countdown from: "))

# Step 2: Get user input for countdown speed
speed = float(input("Enter the countdown speed in seconds (e.g., 1 for normal, 0.5 for fast): "))

# Step 3: Countdown using a while loop
print("\n--- Countdown Begins ---")

while start > 0:
    print(start)
    time.sleep(speed)
    start -= 1

# Step 4: Print final message
print("Countdown Complete!")