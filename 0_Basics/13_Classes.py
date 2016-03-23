# Classes should always start with the capital letter
class Dog():
    """A simple class to represent a dog"""

    def __init__(self, name, age):
        """Initialize names and attributes"""
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.capitalize() + ' is not sitting')

    def roll_over(self):
        print(self.name.capitalize() + ' rolled over')

my_dog = Dog('john', 8)
my_dog.roll_over()
my_dog.roll_over()

# Here is how you can directly change the attribute of a class
my_dog.age = 9

print('\n')
print("My dog's name is " + my_dog.name.capitalize())
print("My dog's age is " + str(my_dog.age))

# Let's create another class for a restaurant

class Restaurant():
    """This class will define the restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print('This restaurant is ' + self.name.capitalize())
        print('This restaurant will serve ' + self.cuisine.capitalize() + ' food')


american_restaurant = Restaurant("Friday's", "american")
american_restaurant.describe()

# Let's create the car class
# For this class you can see make, model, and year are defined by user
# Odometer is assigned the default value from the beginning

class Car():
    """This class will define the car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.capitalize()

    def print_odometer(self):
        print('This car has ' + str(self.odometer) + ' miles on it')

    def update_odometer(self, milage):
        if milage > self.odometer:
            self.odometer = milage
        else:
            print('Do not cheat the system!')

    def increment_odometer(self, increment):
        self.odometer += increment

    def fill_tank(self):
        print('Fill the gas tank')

my_car = Car('mercedes', 'GLA', 2014)
print('\n', my_car.get_name())
my_car.print_odometer()

# we can be modifying attributes of an instance directly

my_car.odometer = 250
my_car.print_odometer()

# you can also update attributes through a method
my_car.update_odometer(500)
my_car.print_odometer()

# we can also be incrementing odometer through the method
my_car.increment_odometer(55)
my_car.print_odometer()

# For class creation we can use inheritance. The original class is parent, the new one is child
# Let's create the class Electric_car that will inherit the attributes from car class
# For child class you can overwrite the method that was defined for the parent class.
# All you have to do is to create the method with the same name.
# In this example we have fill_tank method overwritten

# we can also create class within the class. Let's create class battery and use it with electric car

class Battery():
    """This class defines the battery"""

    def __init__(self, capacity=70): #setting up the default attribute value
        self.capacity = capacity
        self.type = 'lion battery'

    def describe_battery(self):
        print("Battery capacity is " + str(self.capacity))
        print('Battery type is ' + self.type)

class Electric_car(Car):
    """This class defines the electric car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_tank(self):
        print("There is no tank for this car;-)")

my_tesla = Electric_car('tesla', 'model s', 2015)
my_tesla.battery.capacity = 150
my_tesla.battery.describe_battery()

# Right now we will create two classes. Beer is the parent class. Ale is the subclass.

class Beer():
    """This class defines the beer"""

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def show_beer(self):
        print("Beer is " + self.color.capitalize() + ", and it is manufactured by " + self.brand.capitalize())

my_beer = Beer("dark", "heiniken")
my_beer.show_beer()

class Ale(Beer):
    """This class will define ale, based on the beer class"""

    def __init__(self, color, brand, taste = "sweet"):
        super().__init__(color, brand)
        self.taste = taste

    def get_ale(self):
        print('Ale is delicious. Ale is a beer that is ' + self.color + ' and ' + self.brand)

    def get_taste(self):
        print(self.taste)

my_ale = Ale('White', 'IPA')
my_ale.get_ale()
my_ale. show_beer()
my_ale.get_taste()

# more practice

class User():
    """This class defines the users"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.registration_id = 155

    def print_user(self):
        print('User is ' + self.first_name + ' ' + self.last_name)
        print('User registration is', self.registration_id)

user_nikolay = User('Nikolay', 'Poturnak')
user_tatyana = User('Tatyana', 'Poturnak')

user_nikolay.print_user()
user_tatyana.print_user()
print('\n')

class Admin(User):
    """This class defines the administrator"""

    def __init__(self, first_name, last_name, occupation):
        super().__init__(first_name, last_name)
        self.occupation = occupation
        self.privilege = Privileges()

class Privileges():
    """This class defines privileges for the admin user. It accumulates all privilege data"""

    def __init__(self, *privileges):
        self.privileges = []
        for i in privileges:
            self.privileges.append(i)

    def show_privileges(self):
        for i in self.privileges:
            print(i)

admin_1 = Admin(first_name='Nick', last_name='Covalevich', occupation='Coder')
admin_1.privilege = Privileges('Hello')

admin_1.registration_id = 200
admin_1.print_user()
print(admin_1.occupation)
admin_1.privilege.show_privileges()




