filename = input("Enter the filename: ")
filehandle = open(filename)

for line in filehandle:
    # converting into upper case
    uppercase = line.upper()
    # removing new line
    final_line = uppercase.rstrip()
    print(final_line)