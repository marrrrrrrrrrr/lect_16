'''
1. შექმენით პითონის კლასი Car, ატრიბუტებით ბრენდით, მოდელით და წლით. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.

3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car class-ს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".

4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 

5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

'''

from datetime import datetime

class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
    
    # def age_of_car(self, current_year):
    def age_of_car(self):
        # age = current_year - self.year
        age = datetime.now().year - self.year
        return age
    
    def total_cars():
        return Car.number_of_cars
    
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        Car.__init__(self, brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")


# =====================================================================================
        
car1 = Car(brand="Porsche", model="Macan", year=2023)
car2 = Car(brand="Lamborghini", model="Urus", year=2018)

electric_car1 = ElectricCar(brand="BMW", model="i4", year=2022, battery_life=100)

# current_year = 2024

car1.car_info()
car2.car_info()
electric_car1.car_info()

# print(f"{car1.brand}: {car1.age_of_car(current_year)} წელი")
# print(f"{car2.brand}: {car2.age_of_car(current_year)} წელი")
print(f"{car1.brand}: {car1.age_of_car()} წელი")
print(f"{car2.brand}: {car2.age_of_car()} წელი")

# print(f"{electric_car1.brand}: {electric_car1.age_of_car(current_year)} წელი")
print(f"{electric_car1.brand}: {electric_car1.age_of_car()} წელი")

electric_car1.battery_info()

print(f"მანქანების ჯამური რაოდენობა: {Car.total_cars()}")