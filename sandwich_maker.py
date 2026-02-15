
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def _subtract_resources(self, sub_resources):
        #"used to subtract ingredients from resources, does not update resources"
        re_resources = {i: self.machine_resources[i] - sub_resources.get(i,0) for i in sub_resources}
        return re_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # "Also states missing ingredients"
        resource_measure = self._subtract_resources(ingredients)
        # "filters for sub 0 ingredients"
        resource_measure = {i: j for i, j in resource_measure.items() if j < 0}
        # "checks for precence"
        if len(resource_measure) == 0:
            return True
        else:
            print("not enough " + " or ".join(resource_measure.keys()) + ":")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
               Hint: no output"""
        # "assigns appropriate ingredients to sandwich"
        order_ingredients = order_ingredients.get(sandwich_size)
        # "checks ingredients for sandwich"
        if not (self.check_resources(order_ingredients.get("ingredients"))): return
        # "updates resources"
        self.machine_resources = self._subtract_resources(order_ingredients.get("ingredients"))
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
        return self.machine_resources