lines = None
with open('names.txt') as name_file:
    lines = name_file.readlines()

with open('new_names.txt' ,'w') as new_file:
    for line in lines:
        new_file.write(line.replace('\n\n','\n'))

