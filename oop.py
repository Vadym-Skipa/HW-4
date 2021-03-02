# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:

    def __init__(self, max_speed, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage


print(f"{'1.':6}Create a Vehicle class with max_speed and mileage instance attributes\n")

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method


class Bus(Vehicle):

    def set_seating_capacity(self, seating_capacity):
        self._seating_capacity = seating_capacity

    def get_seating_capacity(self):
        if "_seating_capacity" in self.__dict__:
            return self._seating_capacity
        return None


print(f"{'2.':6}Create a child class Bus that will inherit all of the variables and methods of the Vehicle class "
      f"and will have seating_capacity own method\n")

# 3. Determine which class a given Bus object belongs to (Check type of an object)

school_bus = Bus(60)
type_of_school_bus = type(school_bus)

print(f"{'3.':6}Create a school_bus - an instance of the class Bus with a max speed is 60\n"
      f"{'':6}Check the type of the school_bus:  {type_of_school_bus}\n")

# 4. Determine if School_bus is also an instance of the Vehicle class

school_bus_is_Vehicle = isinstance(school_bus, Vehicle)

print(f"{'4.':6}Is school_bus an instance of the class Vehicle?\n"
      f"{'':6}It's {school_bus_is_Vehicle}\n")

# 5. Create a new class School with get_school_id and number_of_students instance attributes


class School:

    def __init__(self, school_id, number_of_students=0):
        self._school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self._school_id


print(f"{'5.':6}Create a new class School with get_school_id and number_of_students instance attributes\n")

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus
# and will have its own - bus_school_color


class SchoolBus(School, Bus):
    def __init__(self, school_id, max_speed, mileage=0, seating_capacity=1, bus_school_color="Yellow",
                 number_of_students=0):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage)
        self.set_seating_capacity(seating_capacity)
        self.bus_school_color = bus_school_color


print(f"{'6.':6}Create a new class SchoolBus that will inherit all of the methods from School and Bus "
      f"and will have its own - bus_school_color\n")

# Polymorphism:
# 7. Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf, make a tuple of it
# and by using for call their action using the same method.


class Bear:

    def make_sound(self):
        print("I'm a bear")


class Wolf:

    def make_sound(self):
        print("I'm not a chihuahua")


bear = Bear()
wolf = Wolf()
animals = (bear, wolf)

print(f"{'7.':6}Create two classes: Bear, Wolf. Both of them should have make_sound method.\n"
      f"{'':6}Create two instances, one of Bear and one of Wolf, make a tuple of it "
      f"and by using for call their action using the same method.\n"
      f"{'':6}Start loop through the tuple")
for animal in animals:
    animal.make_sound()
print(f"{'':6}End of loop\n")

# Magic methods:

# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".


class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population
        print(f"A new instance of the class City initialized with the name {name}")

    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            return "Your city is too small"

    # def __str__(self):
    #     return f"The population of the city {self.name} is {self.population}"


print(f"{'8.':6}Create class City with name, population instance attributes, "
      "return a new instance only when population > 1500, otherwise return message: \"Your city is too small\"\n"
      f"{'':6}Creating Kyiv with a population 3 000 0000")
Kyiv = City("Kyiv", 3000000)
print(f"{'':6}{Kyiv}\n"
      f"{'':6}Creating Lisove with a population 1000")
Lisove = City("Lisove", 1000)
print(f"{'':6}{Lisove}\n")

# 9. Override a printable string representation of the City class
# and return: The population of the city {name} is {population}

City.__str__ = lambda self: f"The population of the city {self.name} is {self.population}"

print(f"{'9.':6}Override a printable string representation of the City class "
      "and return: The population of the city {name} is {population}\n"
      f"{'':6}str(Kyiv): {str(Kyiv)}\n")

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value
# which is greater than 10. And perform this add (+) of two instances.


class task_10:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if self.number > 10 or other.number > 10:
            return task_10(self.number * other.number)
        return task_10(self.number + other.number)


print(f"{'10.':6}Override magic method __add__() to perform the additional action as 'multiply' (*) the value"
      f"which is greater than 10. And perform this add (+) of two instances.\n"
      f"{'':6}A new class with overridden magic method __add__ named task_10\n"
      f"{'':6}task_10(2) + task_10(7) = task_10({(task_10(2) + task_10(7)).number})\n"
      f"{'':6}task_10(2) + task_10(77) = task_10({(task_10(2) + task_10(77)).number})\n")

# 11. The __call__ method enables Python programmers to write classes
# where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.


class task_11:

    def __call__(self, *args):
        result = 0
        for num in args:
            result += num
        return result


my_sum = task_11()
print(f"{'11.':6}The __call__ method enables Python programmers to write classes "
      f"where the instances behave like functions and can be called like a function.\n"
      f"{'':6}A new class with overridden magic method __call__ named task_11\n"
      f"{'':6}my_sum = task_11\n"
      f"{'':6}my_sum(1, 4, 11, 34, -2.3) = {my_sum(1, 4, 11, 34, -2.3)}\n")

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False


class MyOrder:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        return len(self.cart) != 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(f"{'12.':6}Making Your Objects Truthy or Falsey Using __bool__().\n"
      f"{'':6}Create class MyOrder with cart and customer instance attributes.\n"
      f"{'':6}Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.\n"
      f"{'':6}order_1 = MyOrder(['a', 'b', 'c'], 'd')\n"
      f"{'':6}bool(order_1) - {bool(order_1)}\n"
      f"{'':6}order_2 = MyOrder([], 'a')\n"
      f"{'':6}bool(order_2) - {bool(order_2)}")
