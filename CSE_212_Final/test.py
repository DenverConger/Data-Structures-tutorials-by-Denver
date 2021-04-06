#This is to open the file of names
a_file = open("names.txt", "r")

names = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  names.append(line_list)

a_file.close()

a_file = open("loggedin.txt", "r")

logged = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  logged.append(line_list)

a_file.close()
#This is the end of me creating LISTS from the files for you

