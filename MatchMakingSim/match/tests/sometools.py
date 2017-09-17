def readPlayerFile(filename,lines=0):
    #take string filename as argument, open the designated file, return tuple line by line
    with open(filename,"r") as f:
        mylist=list()
       #read the whole file
        if lines==0:
            mylist=[tuple(map(int,i.strip().split(','))) for i in f.readlines()]
        else:
        #read first some lines
            for line in range(lines):
                l=f.readline().strip()
                mylist.append(tuple(map(int,l.split(','))))

    return mylist


