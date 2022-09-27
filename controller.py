import hb_functions as f
import handbook_base as hb
import gui as g

def button_click():
    handbook_temp = hb.read_base()

    # hb.add_new_data(f.new_data(f.new_id(handbook_temp), g.get_lname(), g.get_fname(), g.get_phone_num()))
    

    hb.delete_data(g.get_id(), handbook_temp)