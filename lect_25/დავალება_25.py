# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle

'''
class Book:
    def set_details(self, title, author):
        pass
    def get_discount_price(self, discount):
        pass
'''

class BookDetails:
    def set_details(self, title, author):
        self.title = title
        self.author = author
    
class BookDiscount:
    def __init__(self, book_price):
        self.book_price = book_price

    def get_discount_price(self, discount):
        discounted_price = self.book_price * (1 - discount)
        return discounted_price




# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle
'''
class Payment:
    """  გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
    """
    def process_credit(self, amount):
        pass
'''

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_credit(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_credit(self, amount):
        print(f"Credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_credit(self, amount):
        print(f"PayPal payment of ${amount}")




# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle
'''
class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"
'''


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_capacity(self):
        pass

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"

class FuelVehicle(Vehicle):
    def fuel_capacity(self):
        return "100 liters"




# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
'''
class MultimediaPlayer:
    def play_audio(self):
        pass
    def play_video(self):
        pass
'''

class AudioPlayer:
    def play_audio(self):
        pass

class VideoPlayer:
    def play_video(self):
        pass

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play_audio(self):
        pass
   
    def play_video(self):
        pass




# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
'''
class ConsoleDisplay:
    def show(self, data):
        pass

class WeatherStation:
    def report(self, display):
        display.show("Weather Data")
'''

from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass

class ConsoleDisplay(Display):
    def show(self, data):
        print("Show data on console:", data)

class WeatherStation:
    def report(self, display: Display):
        display.show("Show weather data")