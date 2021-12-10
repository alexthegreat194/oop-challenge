
class Order():
    def __init__(self, type, person):
        self.type = type
        self.person = person
    
    def to_string(self):
        return f"{self.person.name} orders: {self.type}"
        

class Person():
    def __init__(self, name, favorite_drink):
        self.name = name
        self.favorite_drink = favorite_drink

    def my_order(self):
        return Order(self.favorite_drink, self)

class Coffeebar():
    def __init__(self, name, barista):
        self.name = name
        self.orders = []
        self.barista = barista

    def place_order(self, order):
        self.orders.append(order)

    def process_orders(self):
        for order in self.orders:
            print(f'{self.barista.greeting} {order.to_string()}')

class Barista(Person):
    def __init__(self, name, favorite_drink, greeting):
        super().__init__(name, favorite_drink)
        self.greeting = greeting


if __name__ == '__main__':
    person1 = Person('Amy', 'Coffee')
    person2 = Person('Bob', 'Tea')
    person3 = Person('Car', 'Milk')

    barista = Barista('Kevin', 'Coffee', "Hey dude!")

    coffeebar = Coffeebar('chilli\'s', barista)
    
    coffeebar.place_order(person1.my_order())
    coffeebar.place_order(person2.my_order())
    coffeebar.place_order(person3.my_order())
    coffeebar.process_orders()