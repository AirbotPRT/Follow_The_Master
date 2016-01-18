#!/usr/bin/python

import time
import math
import settings
from drone_classes import Drone, DroneSlave

master_d = None
slave_d = None
distance= 0
colinearity=0

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


def calc_distance():
    """
        function used to calculate the distance between two drones.
    """
    distance_x = master_d.x - slave_d.x
    distance_y = master_d.y - slave_d.y
    distance = math.sqrt(distance_x^2 + distance_y^2)

def calc_colinearity():
    """
        function used to calculate the colinearity error between two drones in deg.
    """
    p1x = master_d.x
    p1y = master_d.y
    p2x = master_d.x-distance*math.sin(master_d.o*2*math.pi/360)
    p2y = master_d.y-distance*math.cos(master_d.o*2*math.pi/360)
    p3x = slave_d.x
    p3y = slave_d.y

    p12 = math.sqrt((p1x - p2x)^2 + (p1y - p2y)^2)
    p13 = math.sqrt((p1x - p3x)^2 + (p1y - p3y)^2)
    p23 = math.sqrt((p2x - p3x)^2 + (p2y - p3y)^2)


    colinearity = (math.acos((p12**2 + p13**2 - p23**2) / (2 * p12 * p13)))*(360/(2*math.pi))

#Slave follow the master
def slave_control():
    """
        main program loop
    """
    Drone.refresh_flight_info([master_d, slave_d])  # Don't like that
    check_safety_issues()
    calc_distance()
    calc_colinearity()

    # Altitude fix
    if((master_d.z - settings.MARGIN_ALT) > (slave_d.z + settings.ALT_DIFF)) or ((slave_d.z + settings.ALT_DIFF) > (master_d.z + settings.MARGIN_ALT)):
        slave_d.fix_z(settings.ALT_DIFF)

    # Distance Fix
    elif((settings.DIST - settings.MARGIN_DIST) > distance) or (distance > (settings.DIST + settings.MARGIN_DIST)):
        slave_d.fix_distance(settings.DIST)

    # Orinetation Fix 
    elif((master_d.o - settings.MARGIN_ORIEN) > (slave_d.o + settings.ORIEN_DIFF)) or ((slave_d.o + settings.ORIEN_DIFF) > (master_d.o  + settings.MARGIN_ORIEN)):
        slave_d.fix_o(settings.ORIEN_DIFF)   

    # Coliniearity Fix ( the angle must be 0 if we wants to be colinear)
    elif((settings.COL_DIFF - settings.MARGIN_COL) > colinearity) or (colinearity > (settings.COL_DIFF  + settings.MARGIN_COL)):
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

