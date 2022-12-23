import csv

#1.read data file
csv_file = open('d:\chicago.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
#2.count rows
csv_rows_count = len(csv_file.readlines())
print(csv_rows_count)
#3.if rows conut id odd display correct
if (csv_rows_count % 2) == 0:
    print("{0} is Even number". format(csv_rows_count))
else:
    print("{0} is Odd number". format(csv_rows_count))
#4. if rows count are even display wrong

nationality = 'Sudan'
age = 30

if age<=30 or nationality == 'Egypt':
    print("you can subscribe")
else:
    print("you can not subscribe")


