class Human:
    def __init__(self, country, gender):
        self.country = country
        self.gender = gender

    def sleep(self):
        return f"Go to sleep young {self.gender}"


clara = Human("Nigeria", "Female")
# print(clara.sleep())

david = Human("Nigeria", "Male")
# print(david.gender)


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.retaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.retaurant_name} ")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.retaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"The restaurant has served {self.number_served} customers")

    def increment_number_served(self):
        self.number_served += 1
        print(
            f"The restaurant has served after increment {self.number_served} customers")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'milk', 'strawberry']

    def display_flavors(self):
        print("The flavours: ")
        for flavor in self.flavors:
            print(f"\t {flavor}", end=" ")


ice_cream_stand = IceCreamStand("Ice Cream Paradise", "Ice Cream Shop")

# ice_cream_stand.display_flavors()

restaurant = Restaurant("Open Sharton", "African")
# print(restaurant.number_served)
# restaurant.set_number_served(19)
# restaurant.increment_number_served()

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

restaurant_2 = Restaurant("Roots", "Italian")
restaurant3 = Restaurant("Octopus", "Chinese")

# restaurant_2.describe_restaurant()
# restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name}'s Bio: \n Full name: {self.first_name} { self.last_name} \n Age: {self.age}  \n Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name}, you're welcome")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The number of login attempts is {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(
            f"The number of login attempts after reset is {self.login_attempts}")


class Show_priviledges:
    def __init__(self):
        self.priviledges = ["can add post", "can delete post", "can ban user"]

        def show_priviledges(self):
            print("List of priviledges:")
            for priviledge in self.priviledges:
                print(f"\t{priviledge}")


class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)

        self.show_priviledges = Show_priviledges()


person_1 = Admin("Jane", "Dan", 34, "Female")
person_1.show_priviledges()
# person_1.reset_login_attempts()


# person_1.greet_user()
# print("///////////////")

# person_2 = User("Daniel", "June", 14, "Male")
# person_2.describe_user()
# person_2.greet_user()
# print("////////////////")

# person_3 = User("David", "Nat", 89, "Male")
# person_3.describe_user()
# person_3.greet_user()
# print("///////////////")

# person_4 = User("Liam", "Dan", 34, "Female")
# person_4.describe_user()
# person_4.greet_user()
# print("//////////////")


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.moving = False

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage

    def increase_odometer(self, miles: float):
        self.odometer_reading += miles

    def drive_car(self):
        self.moving = True

    def date_difference(self, current_year):
        difference = current_year - self.year
        print(difference)


my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 50
# my_new_car.read_odometer()

my_new_car.update_odometer(570)
# my_new_car.read_odometer()

my_new_car.update_odometer(0)
# my_new_car.read_odometer()

#########################################
# drive car
# print(f"Is my new car moving {my_new_car.moving}")

# my_new_car.drive_car()
# try:
#     while my_new_car.moving:
#         my_new_car.increase_odometer(10)

# except KeyboardInterrupt:
# with open("speed.txt", "w") as file:
#     odometer = my_new_car.odometer_reading
#     file.write(str(odometer))
# my_new_car.read_odometer()

# my_new_car.read_odometer()


old_car = Car("Peugeot", 408, 1970)
# old_car.date_difference(2024)


####################################
# Inheritance

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
