import random

sips = 5

while sips > 0:
    print("You take a sip... 🧋")
    event = random.choice(["boba pearl!", "brain freeze!", "tea."])
    print("You got:", event)
    sips -= 1

    if event == "boba pearl!":
        print("Yum! You enjoy the chewy boba pearl. 😋")
    elif event == "brain freeze!":
        print("Ouch! You get a brain freeze. 🥶")
        break

    