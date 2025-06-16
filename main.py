### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    class SandwichMachine:
        def __init__(self, machine_resources):
            self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there isn't enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        large_dollar = int(input("How many large dollars?: "))
        half_dollar = int(input("How many half dollars?: "))
        quarter = int(input("How many quarters?: "))
        nickel = int(input("How many nickels?: "))
        total = float(large_dollar * 1.0 + half_dollar * 0.5 + quarter * 0.25 + nickel * 0.05)
        return round(total, 2)

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True

        def make_sandwich(self, sandwich_size, order_ingredients):
            for item in order_ingredients:
                self.machine_resources[item] -= order_ingredients[item]
            print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    ### Make an instance of SandwichMachine class and write the rest of the codes ###

    sammy = SandwichMachine(resources)

    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower().strip()

        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {sammy.machine_resources['bread']} slice(s)")
            print(f"Ham: {sammy.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sammy.machine_resources['cheese']} ounce(s)")
        elif choice in ["small", "medium", "large"]:
            sandwich = recipes[choice]
            if sammy.check_resources(sandwich["ingredients"]):
                payment = sammy.process_coins()
                if sammy.transaction_result(payment, sandwich["cost"]):
                    sammy.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please try again.")