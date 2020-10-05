name = "mbox-short.txt"
handle = open(name)
senders1 = list()
senders = dict()
for line in handle:
    line = line.split()
    # print(line)
    if len(line) < 3 or line[0] != 'From':
        continue
    senders1.append(line[1])
    # print(line[1])
# print(senders1)
for sender in senders1:
    senders[sender] = senders.get(sender, 0) + 1
# print(senders)
maximum = None
theone = None
for sender, count in senders.items():
    # print(sender, count)
    if maximum is None or count > maximum:
        maximum = count
        theone = sender

print(theone, maximum)