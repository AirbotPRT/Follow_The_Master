#!/usr/bin/python

import time
import math
import settings
from drone_classes import Drone, DroneSlave

master_d = None
slave_d = None


#initialize the variables
def init():
    """
        initialisation of the program
    """
    master_d = Drone('/drone1')
    slave_d = DroneSlave('/drone2')

def check_safety_issues():
    """
        function used to check program quit command, or to secure the flight
    """
    pass

#Slave follow the master
def slave_control():
    """
        main program loop
    """
    Drone.refresh_flight_info([master_d, slave_d])
    check_safety_issues()

    # Altitude fix
    if((master_d.z - settings.MARGIN_ALT) > (slave_d.z + settings.ALT_DIFF)) or ((slave_d.z + settings.ALT_DIFF) > (master_d.z + settings.MARGIN_ALT)):
        slave_d.fix_z(settings.ALT_DIFF)

    # Distance Fix
    elif((settings.DIST - settings.MARGIN_DIST) > Drone.calc_distance(master_d, slave_d)) or (Drone.calc_distance(master_d, slave_d) > (settings.DIST + settings.MARGIN_DIST)):
        slave_d.fix_distance(settings.DIST)

    # Orinetation Fix
    elif((master_d.o - settings.MARGIN_ORIEN) > (slave_d.o + settings.ORIEN_DIFF)) or ((slave_d.o + settings.ORIEN_DIFF) > (master_d.o  + settings.MARGIN_ORIEN)):
        slave_d.fix_o(settings.ORIEN_DIFF)

    # Coliniearity Fix ( the angle must be 0 if we wants to be colinear)
    elif((settings.COL_DIFF - settings.MARGIN_COL) > Drone.calc_colinearity(master_d, slave_d)) or (Drone.calc_colinearity(master_d, slave_d) > (settings.COL_DIFF  + settings.MARGIN_COL)):
        slave_d.fix_colinearity(settings.COL_DIFF)



def main():
    """
        Main function of the application
    """
    init()
    while True:
        slave_d.take_off()
        time.sleep(5)# 5 seconds delay
        slave_control()
        time.sleep(5)

def exit_prog():
    """
        Function called before exiting the program
    """
    slave_d.land()

main()
exit()

