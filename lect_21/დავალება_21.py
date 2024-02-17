'''
შექმენით ორი კლასი:
I. Student, ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
II. Address, ატრიბუტებით: city, street


Student კლასის address ატრიბუტს მნიშვნელობად უნდა მიანჭოთ Address კლასის ეგზემპლარი.

შექმენთ ორივე კლასის რამდენინე ეგზემპლარი.

json მოდულის დახმარებით ფაილში შეინახეთ სტუდენტები.

მოახდინეთ წაკითხვა. შეცვალეთ ატრიბუტ(ებ)ის მნიშვნელობა (მაგ.mark, str), დაამატეთ ახალი ატრიბუტი grade მნიშვნელობით A, B, C, D (A -> [91-100], B -> [81-90], C -> [71-80], D -> <=70).

შეცვლილი მონაცემები შეინახეთ ფაილში.

'''


import json
from json import JSONEncoder


class Student:
  row_id = 0

  def __init__(self, name, mark, address):
    self.name = name
    self.mark = mark
    self.address = address
    Student.row_id += 1
    self.row_id = Student.row_id

class Address:
  def __init__(self, city, street):
    self.city = city
    self.street = street


class student_encoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__




address_1 = Address("Tbilisi", "Saburtalo")
address_2 = Address("Tbilisi", "Gldani-7-11-4-93")
address_3 = Address("Tbilisi", "Didube")
address_4 = Address("Tbilisi", "Leselidzs str. 25")
address_5 = Address("Tbilisi", "Guramishvili")
address_6 = Address("Tbilisi", "Varketili IV 407-5-123")

student_1 = Student("Paata", "87", address_1)
student_2 = Student("Demetre", "78", address_2)
student_3 = Student("Alexander", "50", address_3)
student_4 = Student("Teona", "99", address_4)
student_5 = Student("Datuna", "91", address_5)
student_6 = Student("Andria", "78", address_6)


data = [
    {"row_id": student.row_id, "name": student.name, "mark": student.mark, "address": student.address}
    for student in [student_1, student_2, student_3, student_4, student_5, student_6]
]

with open('students_info.json', 'w') as file:
    json.dump(data, file, cls=student_encoder, indent=2)



with open('students_info.json', 'r') as file:
    students = json.load(file)

students[2]["mark"] = "51"
students[2]["address"]["street"] = "Gldani-7-11-4-93"
students[4]["mark"] = "100"

for student in students:
    mark = int(student["mark"])
    if mark >= 91:
        student["grade"] = "A"
    elif mark >= 81:
        student["grade"] = "B"
    elif mark >= 71:
        student["grade"] = "C"
    else:
        student["grade"] = "D"

with open('students_info.json', 'w') as file:
    json.dump(students, file, indent=2)