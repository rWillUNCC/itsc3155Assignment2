#Robert Williams 2/15/26
# ITSC 3155 052 Assignment 2 - Sandwich Maker Modular

import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources.copy())
cashier_instance = Cashier()




def main():

    def runner():
        # "runs the sandwich machine"
        checker = True
        while checker:
            hold = input("What would you like? (small/ medium/ large/ off/ report): ")
            checker = _des_tree(hold)

    def validator(sandwichsize):
        order_ingredients = recipes.get(sandwichsize)
        coins = cashier_instance.process_coins()
        return (cashier_instance.transaction_result(coins, order_ingredients.get("cost")))


    def _des_tree(request):
        # "des tree for the runner"
        match request:
            case "small":
                if validator(request):
                    print("test")
                    sandwich_maker_instance.make_sandwich(request, recipes)
                return True
            case "medium":
                if validator(request):
                    sandwich_maker_instance.make_sandwich(request, recipes)
                return True
            case "large":
                if validator(request):
                    sandwich_maker_instance.make_sandwich(request, recipes)
                return True
            case "off":
                return False
            case "report":
                print("\n".join(f"{i}: {j}" for i, j in sandwich_maker_instance.machine_resources.items()))
                return True
            case _:
                print("input not recognized")
                return True
    ###  write the rest of the codes ###
    runner()

if __name__=="__main__":
    main()
