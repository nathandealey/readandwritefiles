def main():
    outfile = open('philosophers.txt', 'w')
    
    name1 = 'John Locke'
    name2 = 'David Hume'
    name3 = 'Edmond Burke'

    outfile.write(name1 + '\n')
    outfile.write(name2 + '\n')
    outfile.write(name3 + '\n')
    
    outfile.close()

main()