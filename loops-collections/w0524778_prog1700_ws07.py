import random, time

gifts = ["🍫", "🧸", "🎮", "📚", "🎧"]
random.shuffle(gifts)

print("Shuffled gifts:", gifts)
for item in gifts:
    print("You see:", item) 

time.sleep(1)  # Simulate time taken to pick a gift
chosen_gift = random.choice(gifts)
print("You picked:", chosen_gift)
gifts.remove(chosen_gift)
print("Remaining gifts:", gifts)
print("Enjoy your gift!")
# This program simulates a gift selection process.