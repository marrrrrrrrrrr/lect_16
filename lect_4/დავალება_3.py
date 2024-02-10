# '''
# 1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

# '''

# n = int(input("Input number: "))
# sum = 0

# for i in range(1, n + 1):
#     sum += i
# print(sum)



# '''
# 2. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე.

# '''

# n = int(input("Input number: "))

# while n > 0:
#     print(n)
#     n -= 1



# '''
# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი.
# როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.

# '''

# from random import randint
# number = randint(1, 50)

# while True:

#     guess = int(input("Guess the number between 1 and 50: "))

#     if guess == number:
#         print("You guessed the number!")
#         break
#     elif guess > number:
#         print("You guess is greater than the number")
#     else:
#         print("Your guess is lower than the number")



# '''
# 4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს.
# შექმენით საწყისი ცვლადი total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
# ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

# '''

# total_sum = 0

# while True:
#     user_input = input("Enter number: ")
    
#     if user_input == "sum":
#         break
 
#     number = int(user_input)
#     if number > 0:
#         total_sum += number
        
# print(total_sum)