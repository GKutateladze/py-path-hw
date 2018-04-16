import os

dir_list = []
sql_list = []
for root, dirs, files in os.walk("Migrations", topdown=False):
    for name in files:
        dir_name = os.path.join(root, name)
        dir_list.append(dir_name)

    for line in dir_list:
        if line.endswith('.sql'):
            sql_list.append(line)


def find_text(array):
    reduced_array = []
    search_for = input('SEARCH: ')

    for line in array:

        with open (line) as f:
            read_line = f.read()

            if search_for.lower() in read_line.lower():
                reduced_array.append(line)
            else:
                continue

    for reduced_array_line in reduced_array:
        print(reduced_array_line)

    if len(reduced_array) > 1:
        print(f'FOUND {len(reduced_array)} ELEMENTS')
    else:
        print(f'FOUND {len(reduced_array)} ELEMENT')
    if len(reduced_array) == 1:
        return
    find_text(reduced_array)


find_text(sql_list)
