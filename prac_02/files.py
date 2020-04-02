OUTPUT_FILE = "name.txt"
file_out = open(OUTPUT_FILE, "w")
name = str(input("Please enter your name."))
print(name, file=file_out)
file_out.close()

file_in = open("name.txt", "r")
name = file_in.read()
print("Your name is", name)
file_in.close()

file_in = open("numbers.txt", "r")
number1 = file_in.readline()
number2 = file_in.readline()
total = int(number1) + int(number2)
print(total)
file_in.close()

file_in = open("numbers.txt", "r")
total = 0
number3 = file_in.readlines()
for i in number3:
    total += int(i)
print(total)
file_in.close()

