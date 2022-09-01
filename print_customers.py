
import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)
    
for record in csvfile:

    id = record[0]
    FName = record[1]
    LName = record[2]
    City = record[3]
    Country = record[4]
    Phone = record[5]

    print('ID:', id)
    print('First Name: ', FName)
    print('Last Name: ', LName)
    print('City: ', City)
    print('Country: ', Country)
    print('Phone: ', Phone)

    input()