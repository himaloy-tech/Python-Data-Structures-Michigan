name = "mbox-short.txt"
handle = open(name)
senders1 = list()
senders = dict()
for line in handle:
    line = line.split()
    if len(line) < 3 or line[0] != 'From':
        continue
    inde = line[5]
    sp = inde.split(':')
    fi = sp[0]
    senders1.append(fi)
for sender in senders1:
    senders[sender] = senders.get(sender, 0) + 1
bigcount = None
bigword = None
newli = list()
for sender, count in senders.items():
    bigcount = count
    bigword = sender 
    newt = (bigword, bigcount)
    newli.append(newt)
    sortedlist = sorted(newli)
for key, value in sortedlist:
     print(key, value)