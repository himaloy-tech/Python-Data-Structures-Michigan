filename = input("Enter the file name: ")
filehandle = open(filename)
words = []
for line in filehandle:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in words:
            continue
        else:
            words.append(word)
print(sorted(words))