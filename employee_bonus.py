import csv

infile = open("EmployeePay.csv", 'r')
csv_file = csv.reader(infile, delimiter = ',')

next(csv_file)

for record in csv_file:

    id = record[0]
    fname = record[1]
    lname = record[2]
    name = fname + ', ' + lname

    salary = float(record[3])
    bonus = float(record[4])
    bonusamt = bonus*salary

    print()
    print('ID:    ', id)
    print('First Name:    ', fname)
    print('Last Name:    ',lname)
    print('Salary:    ', "${:0,.2f}".format(salary))
    print('Bonus:    ', "${:0,.2f}".format(bonusamt))
    print('Total Pay:    ', "${:0,.2f}".format(salary+bonusamt))
    
    enter = input()
    


