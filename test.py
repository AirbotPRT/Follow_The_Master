#!/usr/bin/python

from drone_classes import Drone

def main():
    """
        test function
    """
    drone_master = Drone("/drone1")
    Drone.refresh_flight_info([drone_master])

main()
