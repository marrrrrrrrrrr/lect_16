chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]




'''
1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის მისამართს, სახელს და შემქნის მას.

'''

import os

def create_file(file_path):
    file = None
    try:
        file = open(file_path, mode = 'x')
    except Exception as e:
        print(f"Error creating file '{file_path}'")
    file.close()

file_path = input("Input the path to the file: ")
create_file(file_path)



'''
2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს

'''

def read_file(file_path):
    file = None
    try:
        file = open(file_path, mode = 'r')
        file_content = file.read()
        return file_content
    except Exception as e:
        print(f"Error reading file '{file_path}'")
    file.close()

file_path = input("Input the path to the file: ")
file_content = read_file(file_path)



'''
3. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს

'''

def update_file(file_path, new_content):
    file = None
    try:
        file = open(file_path, 'a')
        file.write(new_content)
        return new_content
    except Exception as e:
        print(f"Error updating file '{file_path}'")
    file.close()

file_path = input("Input the path to the file: ")
new_content = input("Input the new content: ")
updated_content = update_file(file_path, new_content)



'''
4. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს

'''

import json

def update_file_with_dict(file_path, new_dict_list):
    file = None
    try:
        file = open(file_path, 'r')
        existing_content = json.load(file)

        for new_dict in new_dict_list:
            existing_content.append(new_dict)

        file = open(file_path, 'w')
        json.dump(existing_content, file)
    except Exception as e:
        print(f"Error updating file '{file_path}'")
    file.close()

file_path = input("Input the path to the file: ")
new_dict_list = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

update_file_with_dict(file_path, new_dict_list)
