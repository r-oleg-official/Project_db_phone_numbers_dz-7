import handbook_base as hb
import gui as g

def button_click():
    # path = g.get_path('Path and name of the file: ')
    data = hb.csv_read()
    csv_header = data[0]
    # print(csv_header)
    next_index = hb.csv_index_plus(data)
    print(next_index)
    
    return 0


# def get_path(msg):
#   'To gui.py'
#     return input(msg)

button_click()