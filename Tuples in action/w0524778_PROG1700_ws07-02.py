flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

for origin, destination, price in flights:
    print(f"{origin} → {destination}: ${price}")