from drone_classes import drone, drone_slave
import abstractros


#initialize the variables
def init():
	master_d = NewDrone('/drone1/mavros')
	slave_d = NewDroneSlave ('/drone2/mavros')

#Slave follow the master
def slave_control():
	abstractros.refresh_flight_info([master_d,slave_d])  # Don't like that
	check_safety_issues()
	
	#
	if (master_d.altitude - marginAlt > slave_d.altitude) or (slave_d.altitude > master_d.altitude + marginAlt):
		slave_d.fix_altitude()

	#
	if (master_d.distance - marginDist > slave_d.distance ) or (slave_d.distance  > master_d.distance  + marginDist):
		slave_d.fix_distance()

	# 

	if (master_d.orientation - marginOrien > slave_d.orientation ) or (slave_d.orientation  > master_d.orientation  + marginOrien):
		slave_d.fix_orientation()	

#Main function of the application
def main():
	init()
	while True:
		slave_d.take_off()
		wait(5000)
		slave_control()
		wait(200)

def exit():
	slave_d.land()

main().mainloop()
exit()

