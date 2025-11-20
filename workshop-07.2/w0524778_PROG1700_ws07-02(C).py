scores = {"Alex": 12, "Priya": 18, "Jordan": 9}

while True:
    name = input("Enter the player you want to add to the team (or type 'Done' to finish): ")
    if name.lower() == "done":
        break

    points = int(input(f"Enter the score for {name}: "))
    scores[name] = points

    if points > 20:
        print(f"{name} has leveled up!") 


top_player = max(scores, key=scores.get)
print(f"Top player: {top_player} with {scores[top_player]} points") 


print("\nAll Players:")
for name, points in scores.items():
    print(f"{name}: {points}")

