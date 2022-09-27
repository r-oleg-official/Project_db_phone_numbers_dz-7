import hb_functions as f
import handbook_base as hb
import gui as g

def button_click():
    handbook_temp = hb.read_base()
    while True:
        match g.get_operation():
            case 'new':
                hb.add_new_data(f.new_data(f.new_id(handbook_temp), 
                                            g.get_lname(), 
                                            g.get_fname(), 
                                            g.get_phone_num()))
                print('Запись успешно добавлена!')
            case 'del':
                hb.delete_data(g.get_id(), handbook_temp)
                print('Запись успешно удалена!')
            case 'find':
                print(f.find(g.get_lname(), handbook_temp))
            case 'exit':
                break