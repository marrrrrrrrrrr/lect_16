'''
1. დაწერეთ პროგრამა რომელიც input მეთოდის საშუალებით მიიღებს 2 რიცხვს 
და დააბრუნებს ამ რიცხვებს შორის შესრულებული არითმეტიკული ოპერაციების შედეგებს (მიმატება, გამოკლება, გამრავლება, გაყოფა, ახარისხება)

'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}") 
print(f"{a} ** {b} = {a ** b}")



'''
2. დაწერეთ პროგრამა რომბის ფართობის გამოსათვლელად. მომხმარებელს კლავიატურის გამოყენებით შეაქვს ორი დიაგონალის სიგრძე

'''
d1 = float(input("Enter first diagonal: "))
d2 = float(input("Enter second diagonal: "))

print(f"The area of rhombus = {d1 * d2 / 2}")



'''
3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში

'''

m = int(input("Enter the number of meters: "))

cm = m * 100
dm = m * 10
mm = m * 1000
mi = m / 1609

print(f"{m} meters is equal to {cm} centimeters")
print(f"{m} meters is equal to {dm} decimeters")
print(f"{m} meters is equal to {mm} millimeters")
print(f"{m} meters is equal to {mi} miles")



'''
4. დაწერეთ პროგრამა, რომელიც ითვლის სამკუთხედის ფართობს. მომხმარებელს კონსოლიდან შეყავს სამკუთხედის სიმაღლისა და ფუძის მნიშვნელობა

'''

h = float(input("Enter the height of a triangle: "))
b = float(input("Enter the base of a triangle: "))

print(f"The area of triangle = {h * b / 2}")