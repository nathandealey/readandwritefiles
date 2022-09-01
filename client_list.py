def main ():
    
    infile = open('clients.txt', 'r')
    
    counter = 1

    for line in infile:
        print(counter, ".  ", line.rstrip('\n'),sep='')

        counter += 1
main()

    

         #infile = open('clients.txt', 'r')

    #i = 0
    #for line in infile:
        #i += 1
        #print(str(i)+ '. ' + line.rstrip('\n'))

