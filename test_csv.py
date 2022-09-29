import hb_functions as f
import gui as g
import handbook_base as hb

def csv_click():

    while True:
        match g.get_operation():
            case 'new':      # add
                # path = g.request('Path and name of the file: ')
                path = 'handbook.csv'
                data = g.request('Enter names columns with separator "space": ')
                # print(data)
                hb.create_csv(data, path)
                break
            case 'add':
                path = g.request('Path and name of the file: ')
                path = 'handbook.csv'
                data = hb.csv_read(path)
                csv_header = csv_header(data)
                hb.csv_add_to_id()
                hb.add_new_data(f.new_data(f.new_id(data),
                                            g.get_lname(),
                                            g.get_fname(),
                                            g.get_phone_num()))
                print('Запись успешно добавлена!')
            case 'del':
                path = g.request('Path and name of the file: ')
                path = 'handbook.csv'
                data = hb.csv_read(path)
                csv_header = csv_header(data)


                hb.delete_data(g.get_id(), data)
                print('Запись успешно удалена!')
            case 'find':
                path = g.request('Path and name of the file: ')
                path = 'handbook.csv'
                data = hb.csv_read(path)
                print(f.find(g.get_lname(), data))
            case 'exit':
                break
   

csv_click()