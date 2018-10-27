Ilist = []
Ivar = []
Llist = []
Lvar = []
Mlist = []
Mvar = []

filepath1 = 'tr-heaploop.ref'

with open(filepath1) as fp:
    line = fp.readline()
    while line:
        l = line.split(',')
        check = l[0][:-3]
        if l[1] == 'I':
            if check in Ilist:
                x = Ilist.index(check)
                Ivar[x] += 1
            else:
                Ilist.append(check)
                Ivar.append(1)
        if l[1] == 'L':
            if check in Llist:
                x = Llist.index(check)
                Lvar[x] += 1
            else:
                Llist.append(check)
                Lvar.append(1)
        if l[1] == 'M':
            if check in Ilist:
                x = Mlist.index(check)
                Mvar[x] += 1
            else:
                Mlist.append(check)
                Mvar.append(1)
fp.close()
        
        
