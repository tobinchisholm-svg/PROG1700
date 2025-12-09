import random, time

gifts = ["🍫", "🧸", "🎮", "📚", "🎧"]
random.shuffle(gifts)
while True:
    print("Shuffled gifts:", gifts)
    for item in gifts:
        print("we are removing:", item)
        gifts.pop()

    print(gifts)
