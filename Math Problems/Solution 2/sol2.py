import os
this_folder = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(this_folder,'log')


with open(filename, 'r') as file:
    for line in file:
        if '[ERROR]' in line:
            print(line)
            check.checking(line)

check.display()
