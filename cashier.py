class Cashier:
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