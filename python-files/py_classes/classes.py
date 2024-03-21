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

    def clients_served(self):
        print(f"The restaurant has served {self.number_served} customers")


restaurant = Restaurant("Open Sharton", "African")
restaurant.clients()

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

    def describe_user(self):
        print(f"{self.first_name}'s Bio: \n Full name: {self.first_name} { self.last_name} \n Age: {self.age}  \n Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name}, you're welcome")


# person_1 = User("Jane", "Dan", 34, "Female")
# person_1.describe_user()
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
