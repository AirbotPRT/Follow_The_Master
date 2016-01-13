from drone_classes import Drone, Drone_slave
import abstractros
import settings
import time

master_d=None
slave_d=None


#initialize the variables
def init():
	master_d = Drone('/drone1')
	slave_d = Drone_slave('/drone2')


def check_safety_issues():
	pass


#Slave follow the master
def slave_control():
	abstractros.refresh_flight_info(master_d,slave_d)  # Don't like that
	check_safety_issues()
	
	#
	if (master_d.altitude - settings.marginAlt > slave_d.altitude) or (slave_d.altitude > master_d.altitude + settings.marginAlt):
		slave_d.fix_altitude()

	#
	if (master_d.distance - settings.marginDist > slave_d.distance ) or (slave_d.distance  > master_d.distance  + settings.marginDist):
		slave_d.fix_distance()

	#
	if (master_d.direction - settings.marginDir > slave_d.direction ) or (slave_d.direction  > master_d.direction  + settings.marginDir):
		slave_d.fix_direction()

	# 
	if (master_d.orientation - settings.marginOrien > slave_d.orientation ) or (slave_d.orientation  > master_d.orientation  + settings.marginOrien):
		slave_d.fix_orientation()	

#Main function of the application
def main():
	init()
	while True:
		slave_d.take_off()
		time.sleep(5)# 5 seconds delay
		slave_control()
		time.sleep(5)

def exit():
	slave_d.land()

main()
exit()

