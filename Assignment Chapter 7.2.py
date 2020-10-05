filename = input("Enter the filename: ")
filehandle = open(filename)
total = 0
number_of_lines = 0
for line in filehandle:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    index = line.find(":")
    number_of_lines +=1
    total += float(line[20:].rstrip())

average = total/number_of_lines
print("Average spam confidence:", average)