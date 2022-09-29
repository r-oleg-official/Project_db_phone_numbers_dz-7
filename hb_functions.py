def new_data(id, lname, fname, phone_number):
    return '**'.join([id, lname, fname, phone_number])

def new_id(handbook):
    id_temp = [handbook[i][0] for i in range(len(handbook))]
    id_list = tuple(map(int, id_temp))
    return str(max(id_list) + 1)

def find(lname, handbook):
    lname_list = [handbook[i] for i in range(len(handbook)) if handbook[i][1] == lname]
    return lname_list


# CSV.


def csv_index_plus(data) -> int:
    'Find missed index.'
    for i in range(1, len(data)):
        old_index = int(data[i].split(";")[0])
        if old_index != i: break
    return i


def csv_find_to_id(id, data) -> str:
    "In process. Find element to column by column's name."
    for i in range(1, len(data)):
            print(data[i])

