#1
FILENAME = "name.txt"

# open file for writing
out_file = open(FILENAME, 'w')

# ask the user for their name anc prints
name =  input("Whats your name? >")
print(name, file= out_file)

out_file.close() # close the file

#2
def load_file(filename):
    infile = open(FILENAME, 'r') # open file for reading
    read_file = infile.read()
    print(read_file)
    infile.close()

load_file(FILENAME)

#3
FILENAME = "numbers.txt"

with open(FILENAME, 'r') as infile:
    number_1 = int(infile.readline()) # used readline to read separate lines
    number_2 = int(infile.readline())
print(number_1 + number_2)

#4

with open(FILENAME, 'r') as infile:
    total = 0
    for line in infile:
        number = int(line.strip())
        total += number
    print(f"Sum total is {total}")




