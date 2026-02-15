class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        """Returns the total calculated from coins inserted.
                   Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please enter coins")
        total = int(input("how many large dollars?: ") or 0) * 1.
        total += int(input("how many half dollars?: ") or 0) * .5
        total += int(input("how many quarters?: ") or 0) * .25
        total += int(input("how many nickels?: ") or 0) * .05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            print(f"Here is {coins - cost:.2f} in change")
            return True
