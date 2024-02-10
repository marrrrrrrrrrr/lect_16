'''
1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]),
თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი;
თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი;
'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა,
მიღებული შედეგი დაბეჭდეთ კონსოლში.

მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:

a – append

r – remove

e – exit

მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.

'''

my_list = []
    
while True:
    command = input("a – append \nr – remove \ne – exit \nInput one of the commands above: ").lower()

    if command == "e":
        break
    elif command == "a":
        my_list.append(int(input("Input your number: ")))
    elif command == "r":
        num = int(input("Input number to remove: "))
        if num in my_list:
            my_list.remove(num)
        else:
            print("This number is not in the list\n")
    else:
        print("Wrong command")
print(my_list)




# '''
# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს შემდეგ ნაბიჯებს:

# a. დაბეჭდავს 210-ის ინდექსს;

# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;

# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

# '''


# my_list = [43, '22', 12, 66, 210, ["hi"]]

# #a
# print(f"Index of 210 is {my_list.index(210)}")
# #b
# my_list[5].append("Hello")
# #c
# del my_list[2]
# print(my_list)
# #d
# my_llist_2 = my_list.copy()
# my_llist_2.clear()
# print(f"my_list: {my_list}")
# print(f"my_llist_2: {my_llist_2}")



# '''
# 3. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს,
# თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

# '''

# import re

# num = input("Input phone number: ")
# # num = "(123) 456-789"
# pettern = r"^\(\d{3}\) \d{3}-\d{3}$"

# result = re.match(pettern, num)
# if result:
#     print(result.group())
# else:
#     print("Invalid format")