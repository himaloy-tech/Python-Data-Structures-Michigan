filehandle = open('mbox-short.txt')
number_of_lines = 0
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From:'):continue
    line = line.split()
    number_of_lines += 1
    print(line[1])

print("There were", number_of_lines, "lines in the file with From as the first word")
