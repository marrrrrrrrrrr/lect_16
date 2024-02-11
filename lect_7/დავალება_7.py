'''
1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას

'''

def fibonnaci(n):
    A = []
    for i in range (n + 1):
        if i == 0:
            A.append(0)
        elif i == 1:
            A.append(1)
        else:
            A.append(A[i-1] + A[i-2])
    return A

n = int(input("Enter the number: "))
result = fibonnaci(n)
print(f"First {n} numbers of Fibonacci sequence are: {result}")




'''
2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
(ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

'''

def anagram(str1, str2):
    for i in str1:
        if str2.find(i) == -1 or len(str1) != len(str2):
            print(f"{str1} and {str2} are not anagrams")
            return
    print(f"{str1} and {str2} are anagrams")

anagram("listen", "silent")
anagram("on", "non")




'''
3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

'''

def factorial(n):
    if n < 0:
        print("Factorial of a negative number is not defined")
        return None
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

n = int(input("Enter the number: "))
result = factorial(n)
print(f"Factorial of {n} is {result}")




'''
4. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს.
ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.

'''

def count_char(str1, ch1):
    count = 0
    for char in str1:
        if char == ch1:
            count += 1
    return count

res = count_char("abcde fgg  gg", " ")
print(f"Count of character in the string: {res}")