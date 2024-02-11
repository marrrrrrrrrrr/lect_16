'''
1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფომრაციას (id,name,age,grade,subject_name,marks) და თქვენ სტუდენტს დაამატებთ csv ფაილში.
2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
3. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.

'''


import os, csv

def create_csv(path, file_name):
    file_path = f"{path}/{file_name}.csv"
    
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"Folder '{path}' exisis")
        print("Continue working...\n")


    try:
        with open(file_path, 'x', encoding = 'utf-8') as file:
            header = ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
    except FileExistsError:
        print(f"File '{file_path}' exisis")
        print("Continue working...\n")


def create_data():
    data = [
        ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
    ]

    id = 1

    while True:
        name = input("Name: ")

        if not name:
            print()
            break

        age = int(eval(input("Age: ")))
        grade = input("Grade: ")
        subject = input("Subject: ")
        mark = int(eval(input("Mark: ")))

        data.append([id, name, age, mark, subject, grade])

        id +=1

        print(f"\n{data}\n")

    return data


def add_students(path, data):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)

        csv_writer.writerows(data)


def read_data(path, student_name=''):
    with open(path, 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))

    if not student_name:
        return reader
    
    st_row = [['id', 'name', 'age', 'grade', 'subject_name', 'marks']]

    for row in reader:
        if row[1] == student_name:
            st_row.append(row)

    return st_row


def update_mark(path, id, subject, mark):
    data = read_data(path)

    for row in data[1]:
        if int(row[0]) == id and row[4] == subject:
            row[5] == mark
            break
        else:
            print("Can't update")

    add_students(path, data)


path = 'csv_files'
file_name = 'csv_data1'
file_path = create_csv(path, file_name)

# data = create_data()
# print(data)

# add_students(file_path, data)

# file_content = read_data(file_path, "Mariam")
# print(file_content)

# id = 1
# subject = 'Math'
# mark = 100
# update_mark(file_path, id, subject, mark)