def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(f"Pizza toppings are: {toppings}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def pizza_making(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


pizza_making('pepperoni')
pizza_making('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')