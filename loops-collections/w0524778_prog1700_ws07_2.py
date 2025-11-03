route = [("Start", "Park"), ("Park", "Cafe"), ("Cafe", "Library")]
for frm, to in route:  # tuple unpacking
    print(f"{frm} → {to}")
