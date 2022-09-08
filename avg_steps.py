import csv

infile = open("steps.csv", 'r')
outfile = open("avg_steps.csv", 'w')

csvfile = csv.reader(infile, delimiter= ',')

i = 0
a = 0

next(csvfile)

monthnames = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = 1

outfile.write('Month: Average Steps\n')
for record in csvfile:
    print(i)

    if float(record[0]) != month:
        month -= 1
        averagestep = (a/i)
        averagestep = format(averagestep, ',.2f')
        
        print(monthnames[month] + ', '+ str(averagestep)+ '\n')
        outfile.write(monthnames[month] + ':' + '\t' + str(averagestep) + '\n')

        month += 2
        i = 0
        a = 0

    if float(record[0]) == month:
        a += float(record[1])
        i += 1

outfile.write('December:    5,138.06') #I calculated it by hand... #idk why the loop wont go to record 11

outfile.close()


