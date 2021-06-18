my_file = open("globals.txt", "r")
file_data = my_file.readlines()
string = ""
for i in file_data:
  string += i

print(repr(string))
