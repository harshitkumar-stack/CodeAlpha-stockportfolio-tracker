
portfolio = []

print("=== Stock Portfolio Tracker ===")

while True:
    name = input("\nEnter stock name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per share: "))

        if quantity <= 0 or price < 0:
            print("Please enter valid positive values.")
            continue

        investment = quantity * price

        portfolio.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        print(f"Investment in {name}: Rs. {investment:.2f}")

    except ValueError:
        print("Please enter numbers for quantity and price.")

print("\n=== Your Portfolio ===")

total = 0

for stock in portfolio:
    print(
        f"{stock['name']}: {stock['quantity']} shares "
        f"x Rs. {stock['price']:.2f} = "
        f"Rs. {stock['investment']:.2f}"
    )
    total += stock["investment"]

print(f"\nTotal Investment: Rs. {total:.2f}")

with open("portfolio.txt", "w") as file:
    for stock in portfolio:
        file.write(
            f"{stock['name']}, {stock['quantity']}, "
            f"{stock['price']}, {stock['investment']:.2f}\n"
        )

print("Portfolio saved to portfolio.txt")
