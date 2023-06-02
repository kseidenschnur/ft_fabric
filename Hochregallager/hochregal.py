import configparser
import time
import threading
import queue
from move import *

# get values from the configuration file
config = configparser.ConfigParser()
config.read('calibration.conf')

col_a = int(config['HOCHREGALLAGER']['col_a'])
col_b = int(config['HOCHREGALLAGER']['col_b'])
col_c = int(config['HOCHREGALLAGER']['col_c'])
get_cell_1 = int(config['HOCHREGALLAGER']['get_cell_1'])
get_cell_2 = int(config['HOCHREGALLAGER']['get_cell_2'])
get_cell_3 = int(config['HOCHREGALLAGER']['get_cell_3'])
drop_cell_1 = int(config['HOCHREGALLAGER']['drop_cell_1'])
drop_cell_2 = int(config['HOCHREGALLAGER']['drop_cell_2'])
drop_cell_3 = int(config['HOCHREGALLAGER']['drop_cell_3'])
vg_cb_turn = int(config['VAKUUMGREIFER']['vg_cb_turn'])
vg_cb_forth = int(config['VAKUUMGREIFER']['vg_cb_forth'])
vg_cb_down = int(config['VAKUUMGREIFER']['vg_cb_down'])
vg_ho_turn = int(config['VAKUUMGREIFER']['vg_ho_turn'])
vg_ho_forth = int(config['VAKUUMGREIFER']['vg_ho_forth'])
vg_ho_down = int(config['VAKUUMGREIFER']['vg_ho_down'])


#Creating list of positions for loop
positions = [['a1', col_a, get_cell_1, drop_cell_1], ['a2', col_a, get_cell_2, drop_cell_2], ['a3', col_a, get_cell_3, drop_cell_3],\
             ['b1', col_b, get_cell_1, drop_cell_1], ['b2', col_b, get_cell_2, drop_cell_2], ['b3', col_b, get_cell_3, drop_cell_3],\
             ['c1', col_c, get_cell_1, drop_cell_1], ['c2', col_c, get_cell_2, drop_cell_2], ['c3', col_c, get_cell_3, drop_cell_3]]

# Create queue for multi-threading
tqueue = queue.Queue()

######################################################################################################################################

for cell_count in range(len(positions)):
    
    t_moveVGGrab = threading.Thread(target=moveVGGrab, args=(cell_count,tqueue,vg_cb_turn,vg_cb_forth,vg_cb_down,vg_ho_turn,vg_ho_forth,vg_ho_down,))
    
    cell_name = positions[cell_count][0] 
    col = positions[cell_count][1]
    get_cell = positions[cell_count][2]
    drop_cell = positions[cell_count][3]

    moveHBWReset()
    moveHBWGet(cell_name,col,get_cell)
    moveHBWGrab()
    moveHBWDeliver()

    if tst_a4.state() == 0:

        t_moveVGGrab.start()

        mtr_a4.setSpeed(-512)
        while tst_a1.state()!=0:
            txt.updateWait()
        time.sleep(0.5)
        mtr_a4.stop()

    tresult = tqueue.get()

    if tst_a1.state() == 0:
        mtr_a4.setSpeed(512)
        while tst_a4.state()!=0:
            txt.updateWait()
        mtr_a4.stop()

    moveHBWBack(cell_name,col,drop_cell)
    moveHBWDrop()