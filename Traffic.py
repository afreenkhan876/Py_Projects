from enum import Enum

# Step 1: Create the Enum
class TrafficSignal(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

# Step 2: Ask user to enter signal
signal = input("Enter traffic signal (RED / YELLOW / GREEN): ").upper()

# Step 3: Check and respond
if signal == "RED":
    print("Stop! 🚫")
elif signal == "YELLOW":
    print("Slow down! ⚠️")
elif signal == "GREEN":
    print("Go! ✅")
else:
    print("Invalid signal! Please enter RED, YELLOW, or GREEN.")