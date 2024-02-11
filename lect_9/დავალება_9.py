'''
1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

'''

# zip_arrs = lambda arr1, arr2: list(zip(arr1, arr2))

# arr1 = [1, 2, 3]
# arr2 = ['a', 'b', 'c']

# print(zip_arrs(arr1, arr2))



'''
2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.

'''

# from functools import reduce

# def multiply(arr1):
#     try:
#         product = reduce(lambda x, y: x * y, arr1)
#         print(product)
#     except TypeError as ex:
#         print(ex)

# arr1 = [1, 2, 3, 4, 5, 6]
# multiply(arr1)




'''
3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

'''

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 66, 5, 44, 3, 6, 77, 1230]
# is_odd = list(filter(lambda x: x % 2 == 1, arr))
# print(f"Odd elements of the list are: {is_odd}")




'''
4. დაწერეთ პითონის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

'''

# def func(arr1, str1):
#     try:
#         word = list(filter(lambda x: x.endswith(str1), arr1))
#         print(*word)
#     except TypeError as ex:
#         print(ex)
#     except:
#         print("An exception")
        

# arr1 = ["A", "AB", "ABC", "BCA", "BA", "AC", "CA"]
# str1 = "A"

# func(arr1, str1)
