from datetime import datetime as dt
import gui as g
import hb_functions as f

# Добавление записи:
def add_new_data(data):
    with open('handbook.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data}**\n')

# Считывание базы данных из .txt
def read_base():
    with open('handbook.txt', 'r', encoding="utf-8") as file:     
        data = file.readlines()
    data = [data[i][:-1].split('**') for i in range(len(data))]
    data = [data[i][1:-1] for i in range(len(data))]
    return data

# Удаление записи из базы данных .txt 
def delete_data(id, data):    
    data = ['**'.join(data[i]) for i in range(len(data)) if int(data[i][0]) != int(id)]
    with open('handbook.txt', 'w', encoding="utf-8") as file:
        for i in range(len(data)):
            file.write(f'**{data[i]}**\n')

# CSV.
def create_csv(data, path_file = 'handbook.csv'):
    'Create a new empty handbook.'
    with open(path_file, 'w', encoding="utf-8") as file:
        file.write(data.replace(' ', ';'))


def csv_header(data) -> str:
    return data[0].split(';')


def csv_read(path_file = 'handbook.csv') -> str:
    with open(path_file, 'r', encoding="utf-8") as csvfile:     
        data = csvfile.readlines()
    return data

def csv_add(data, path_file = 'handbook.csv') -> str:
    'In process. Add record by id.'
    #id = f.csv_index_plus(data)
    #print(id)
    with open(path_file, 'w', encoding="utf-8") as file:
        file.write(f'{csv_header(data)}')
        file.write(f'{data}')
    return data

def csv_del_to_id(id, data) -> str:
    'In process. Delete record by id.'
    for i in range(1, len(data)):
        old_index = int(data[i].split(";")[0])
        if old_index != i: break
    return i
    
