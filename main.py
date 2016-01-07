import drone_slave
import drone
import abstract.ros


#initialize the variables
def init():
	master_d = NewDrone('/drone1/mavros')
	slave_d = NewDroneSlave ('/drone2/mavros')

#Slave follow the master
def slave_control():
	ros.get_flight_info([master_d,slave_d])
	check_safety_issues()
	
	# If The slave attitude (Margin included) different Master altitude (Margin Included) => fix_altitude()
	if (slave_d.altitude - MarginAlt or slave_d.altitude + MarginAlt) != master_d.altitude:
		slave_d.fix_altitude()

	# If The slave distance (Margin included) different Master distance => fix_distance()
	if (slave_d.distance - MarginDist or slave_d.distance + MarginDist) != master_d.distance:
		slave_d.fix_distance()

	# If The slave orientation (Margin included) different Master orientation => fix_orientation()
	if (slave_d.orientation - MarginOrien or slave_d.orientation + MarginOrien) != master_d.orientation:
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

