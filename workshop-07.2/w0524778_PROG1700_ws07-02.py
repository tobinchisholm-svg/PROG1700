groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}



while True: 
    item = input("Enter an item name (or type'exit' to finish):")
    if item.lower().strip() == 'exit':
        break
    try:
        price = float(input(f"enter the price for the {item}: "))
        #updating the gorcery list
        groceries[item] = price 
    except ValueError:
        print("invalid price. please enter a number value.")
    total = 0
    highest_price=0
    for item, price in groceries.items():
        print(f"{item:10} ${price:5.2f}")
        total += price
        if price > highest_price:
            highest_price = price
            most_expensive_item = item

    print(f"\nTotal cost: ${total:.2f}")
    print(f"the most expensive item in the grocery list is: {most_expensive_item}at ${highest_price:.2f}")
        
        