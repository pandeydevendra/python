"""A set of classes used to represent gas and electric cars."""

from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    my_tesla.read_odometer()
    my_tesla.update_odometer(10)
    my_tesla.read_odometer()
    my_tesla.increment_odometer(5)
    my_tesla.increment_odometer(5)
    my_tesla.read_odometer()
    my_tesla.battery.describe_battery()
    my_tesla.fill_gas_tank()
    my_tesla.increment_odometer(5)
    my_tesla.increment_odometer(5)
    my_tesla.read_odometer()
    my_tesla.battery.describe_battery()
    my_tesla.fill_gas_tank()
    my_tesla.battery.get_range()
