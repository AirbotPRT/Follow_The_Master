#!/usr/bin/python

import math
import abstractros
from drone_classes import *

def main():
    """
        test function
    """
    drone_master = Drone("/test")
    drone_slave = DroneSlave("/drone1")
    drone_slave.set_master(drone_master)
    Drone.refresh_flight_info([drone_slave])
    abstractros.arm(drone_slave)


main()
