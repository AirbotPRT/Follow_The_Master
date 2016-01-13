#!/usr/bin/python
import abstractros
from drone_classes import Drone
	
def main():
	drone_master = Drone("/drone1/mavros")
	abstractros.refresh_flight_info([drone_master])

main()
