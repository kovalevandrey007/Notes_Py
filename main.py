import csv

from datetime import datetime

import pandas as pd

# with open('csv.csv') as File:
#     reader = csv.reader(File, delimiter=',')
#     for row in reader:
#         print(row)

# results = []
# with open('csv.csv') as File:
#     reader = csv.DictReader(File)
#     for row in reader:
#         results.append(row)
#     print (results)
#
# myData = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]
# myFile = open('example2.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)
#
# print("Writing complete")
name = input("Введите имя нового файла: ")
with open(f'{name}.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    my_dict = {}
    my_dict['first_name'] = input("Введите имя: ")
    my_dict['last_name'] = input("Введите Фамилию: ")
    my_dict['Grade'] = input("Введите числа: ")
    writer.writerows([my_dict])
print("writing complete")


results = []
with open(f'{name}.csv') as File:
    reader = csv.DictReader(File)
    for line in reader:
        results.append(line)
    print (results)

filename = "a.csv"
# очистка файла a.csv
f = open(filename, "w+")
f.close()


def date_key(row):
    return datetime.strptime(row[1].strip(), "%m/%d/%Y")
    with open('\\home\\Andy-PC\\PycharmProjects\\pythonProject1\\', 'rb') as f:
        data = list(csv.reader(f))
    print(data)

data = pd.read_csv('ex.csv')
data['Time'] = pd.to_datetime(data['Time'], format="%m.%d.%Y %H:%M")

data = data.sort_values(by='Time', ascending=False)
print(data.to_csv(index=False))

# data.sort_values(by = 'date', ascending = True, inplace = True)
# display(data.head())

# name = input("Введите новое имя файла: ")
# with open(f'{name}.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# with open("test.csv", "r", newline = "") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter = ";")
#     for row in reader:
#         print(row['имя'], "|", row['тел'], "|", row[' число'])
#
# # Запись файла
# name = input("Введите название файла:")
# with open(f"{name}.csv", "w", newline = "") as csvfile:
#      header = ["число", "слово", "тел"]
#      writer = csv.writer(csvfile)
#      for line in reader:
#          writer.writerow(line[input()], line[input()], line[input()])
#     # writer = csv.writer(csvfile, delimiter = ";")
    # writer.writerow([row["23"],row["zxc"], row["1111"]])

    # writer.writerow(["23","zxc", "1111"])
    # writer.writerow(["34","qwe","2222"])


# with open("qwerty.csv", "r") as f:
#     reader = csv.DictReader(f)
# 
#     with open("new.csv", "w") as f:
#         header = ["число", "слово", "тел"]
#
#         writer.writeheader()
# 
#         for line in reader:
#             writer.writerow(line["11"], line["qqqq"], line["9000"])
# file_name = input("Введите имя файла: ")
# def write_data(file_name):
#       # запись данных в файл
#     with open(file_name, "w", newline = "") as file:
#         writer = csv.writer(file, delimiter = ";")
#         writer.writerow(["number", "name", "phone"])
#         for i in range(1,5):
#             writer.writerow(["1"*i, "2"*i, "3"*i])
#
# def reader_data(file_name):
#     # считывание файла .csv
#     with open(file_name, newline = "") as file:
#         reader = csv.reader(file, delimiter = ";")
#         for row in reader:
#             print(row)
# # #
# # if __name__ == '__main__':
# #     reader_data("ex.csv")