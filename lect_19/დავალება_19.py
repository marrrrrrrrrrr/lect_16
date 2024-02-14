'''
1. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

2. Car კლასს დაუმატეთ თითეული ატრიბუტისთვის set და get ფუნქციები მათი ცვლილებებისთვის.

3. დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის ინტეგერი და ასე შემდეგ.

'''


class Car:
  def __new__(cls, *args, **kwargs):
    instance = super().__new__(cls)

    return instance


  def __init__(self, brand = None, model = None, year = None):
    self._brand = brand
    self._model = model
    self._year = year

  @property
  def brand(self):
    return self._brand
  
  @property
  def model(self):
    return self._model
  
  @property
  def year(self):
    return self._year
  
  @brand.setter
  def brand(self, value):
    if isinstance(value, str):
      self._brand = value
    else:
      raise ValueError("Brand name should be a string")
    
  @model.setter  
  def model(self, value):
    if len(value) < 50:
      self._model = value
    else:
      raise ValueError("Model name is too long")
  
  @year.setter
  def year(self, value):
    if isinstance(value, int) and value > 0:
      self._year = value
    else:
      raise ValueError("Year should be positive integer")
  


car = Car()
car.brand = "Alfa Romeo"
car.model ="105"
car.year =1977
print(car.brand)
print(car.model)
print(car.year)