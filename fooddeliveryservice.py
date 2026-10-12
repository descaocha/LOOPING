import time

available_pizzas = ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken"]
pizza_order = []
total_price = 0
PIZZA_PRICE = 10

print("Hello!")
time.sleep(2)

# ---- Loop 1: menu -> pilih pizza -> mau beli lagi? ----
while True:
    print("\nAvailable pizzas:")
    for number, pizza in enumerate(available_pizzas):
        print(f"{number}. {pizza}")

    try:
        pizza_choice = int(input("What pizza do you want? (provide a number): "))
    except ValueError:
        print("Please choose a correct number.")
        continue

    if 0 <= pizza_choice < len(available_pizzas):
        item = available_pizzas[pizza_choice]
        pizza_order.append(item)
        total_price += PIZZA_PRICE
        print(f"Adding {item} pizza to the list")
    else:
        print("Please choose a correct number.")
        continue

    again = input("Do you want to order another pizza? (yes/no): ").strip().lower()
    if again != "yes":
        break

print(f"\nYour order: {', '.join(pizza_order)}")
print(f"U have to pay {total_price} $.")
time.sleep(2)

# ---- Loop 2: tip (ulang hanya kalau input salah) ----
while True:
    try:
        tip = float(input("What tip do you want to leave (0-25%)?: "))
        if 0 <= tip <= 25:
            break
    except ValueError:
        pass
    print("Please provide a correct number.")

total_price += total_price * tip / 100
print(f"Thank you! The price is now {total_price} $. Pizzas r on the way")