## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a attribute named name
        self.name = name

## Cat is-a animal
class Cat(Animal):
    ## Cat has a funciton called __init__
    def __init__(self, name):
        ## Cat has-an attribute named name
        self.name = name

## Class Person is an object
class Person(object):
    def __init__(self, name):
        self.name = name

        ## Person has a pet of some kind
        self.pet = None

## Class Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        ## Employee has-an attribute named salary
        self.salary = salary

## Class Fish is-an object
class Fish(object):
    pass

## Class Salmon is-a fish
class Salmon(Fish):
    pass

## Class Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has a pet named Satan
mary.pet = satan

## Frank is an employee
frank = Employee("Frank", 120000)

## Frank has a pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## Harry is a halibut, of course
harry = Halibut()