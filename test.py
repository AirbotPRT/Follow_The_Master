#!/usr/bin/env python

import abstractros
import time
from drone_classes import Drone, DroneSlave

def main():
    """
        test function
    """

    print "creating drone master...\n"
    drone_master = Drone("/test")

    print "creating drone slave...\n"
    drone_slave = DroneSlave("/drone1")

    print "set master...\n"
    drone_slave.set_master(drone_master)

    print "refresh flight infos...\n"
    Drone.refresh_flight_info([drone_slave])

    # print "drone coordinates :"
    # print drone_slave.x
    # print drone_slave.y
    # print drone_slave.z
    # print drone_slave.o

    # print "arm slave...\n"
    # print abstractros.arm(drone_slave)
    # time.sleep(2)
    # print "disarm slave...\n"
    # print abstractros.disarm(drone_slave)
    # time.sleep(2)
    # print "takeoff slave...\n"
    # print abstractros.takeoff(drone_slave)
    # time.sleep(2)
    # print "land slave...\n"
    # print abstractros.land(drone_slave)
    # time.sleep(2)
    # print "slave goto...\n"
    # print abstractros.goto(drone_slave, 1, 1, 1, 1)
    # time.sleep(2)

main()
