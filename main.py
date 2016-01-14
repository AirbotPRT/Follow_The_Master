#!/usr/bin/python

import time
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
    Drone.refresh_flight_info([master_d, slave_d])  # Don't like that
    check_safety_issues()
    
    #
    if((master_d.altitude - settings.MARGIN_ALT) > slave_d.altitude) or (slave_d.altitude > (master_d.altitude + settings.MARGIN_ALT)):
        slave_d.fix_altitude()

    #
    if((master_d.distance - settings.MARGIN_DIST) > slave_d.distance) or (slave_d.distance > (master_d.distance + settings.MARGIN_DIST)):
        slave_d.fix_distance()

    #
    if((master_d.colinearity - settings.MARGIN_COL) > slave_d.colinearity) or (slave_d.colinearity > (master_d.colinearity  + settings.MARGIN_COL)):
        slave_d.fix_colinearity()

    # 
    if((master_d.orientation - settings.MARGIN_ORIEN) > slave_d.orientation) or (slave_d.orientation > (master_d.orientation  + settings.MARGIN_ORIEN)):
        slave_d.fix_orientation()   

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

