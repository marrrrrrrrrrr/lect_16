'''
1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია,
რომელიც მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

'''

int_list = [10, 20, 30, 40]

def add_to_list(num):
    global int_list
    int_list.append(num)
    return int_list

number_to_add = int(input("Input number: "))
print(add_to_list(number_to_add))



'''
2. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

'''

number_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def sum_list(input_list):
    sum = 0
    for num in input_list:
        sum += num
    return sum

print(f"The sum of the numbers is: {sum_list(number_list)}")



'''
3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია,
რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

'''

gl_str = "Global"

def func(par1):
    gl_str = "Local"
    return gl_str

print(func(gl_str))



'''
4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number
და დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

'''

def sum_digits(number):
    if number < 10:
        return number
    
    return number % 10 + sum_digits(number // 10)

result = int(input("Input number: "))
print(f"The sum of the digits is: {sum_digits(result)}")



'''
5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს
და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)

'''

def reverse(str1):
    if len(str1) <= 1:
        return str1
    return str1[-1] + reverse(str1[:-1])

result = reverse(input("Input string: "))
print(f"The reverse of the string is: {result}")
    