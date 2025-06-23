import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

sandwich_maker = SandwichMaker(data.resources)
cashier = Cashier()

while True:
    choice = input("What would you like? (small/medium/large/off/report): ").lower().strip()

    if choice == "off":
        break
    elif choice == "report":
        print(f"Bread: {sandwich_maker.machine_resources['bread']} slice(s)")
        print(f"Ham: {sandwich_maker.machine_resources['ham']} slice(s)")
        print(f"Cheese: {sandwich_maker.machine_resources['cheese']} ounce(s)")
    elif choice in ["small", "medium", "large"]:
        sandwich = data.recipes[choice]
        if sandwich_maker.check_resources(sandwich["ingredients"]):
            payment = cashier.process_coins()
            if cashier.transaction_result(payment, sandwich["cost"]):
                sandwich_maker.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid choice. Please try again.")