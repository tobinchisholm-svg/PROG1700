ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

departure, arrival, flight, cost = ticket

print(f"From {departure} to {arrival} on flight {flight} costing ${cost}")