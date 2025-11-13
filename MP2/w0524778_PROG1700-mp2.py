import random



score = {"player": 0, "cpu": 0, "ties": 0}



winning_moves = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

valid_moves = ["rock", "paper", "scissors", "lizard", "spock"]


shortcut = {"r": "rock", "p": "paper", "s": "scissors", "l": "lizard", "sp": "spock"}




while True:
    get_player_move = input("Choose rock (R), paper (P), scissors (S), lizard (L), spock (SP) or Q to quit: ").lower().strip()

   
   
   
    if get_player_move == "q":
        print("Game over!")
        print(f"Final Score -> Player: {score['player']} | CPU: {score['cpu']} | Ties: {score['ties']}")
        break

   
    if get_player_move in shortcut:
        get_player_move = shortcut[get_player_move]

    if get_player_move not in valid_moves:
        print("Invalid choice!")
        continue

    get_cpu_move = random.choice(valid_moves)
    print("CPU chose:", get_cpu_move)

    if get_player_move == get_cpu_move:
        print("It's a tie!")
        score["ties"] += 1
    elif get_cpu_move in winning_moves[get_player_move]:
        print("You win!")
        score["player"] += 1
    else:
        print("CPU wins!")
        score["cpu"] += 1

   
   
   
    print(f"Score -> Player: {score['player']} | CPU: {score['cpu']} | Ties: {score['ties']}")