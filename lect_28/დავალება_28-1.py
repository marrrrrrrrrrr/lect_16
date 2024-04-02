# დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე


import threading

def search_even():
  even_numbers = []
  for num in range(30, 51):
      if num % 2 == 0:
          even_numbers.append(num)
  print("Even numbers between 30 and 50:", even_numbers)

def search_odd():
  odd_numbers = []
  for num in range(30, 51):
      if num % 2 != 0:
          odd_numbers.append(num)
  print("Odd numbers between 30 and 50:", odd_numbers)


even_t1 = threading.Thread(target=search_even)
odd_t1 = threading.Thread(target=search_odd)

even_t1.start()
odd_t1.start()

even_t1.join()
odd_t1.join()