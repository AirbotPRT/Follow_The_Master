import drone_slave
import drone
import abstract.ros


#initialize the variables
def init():
	master_d = NewDrone('/drone1/mavros')
	slave_d = NewDroneSlave ('/drone2/mavros')

#Slave follow the master
def slave_control():
	ros.get_fligh_info([master_d,slave_d])
	check_safety_issues()
	slave_d.fix_altitude()
	# If TODO 
		

#Main function of the application
def main():
	init()
	while True:
		slave_d.take_off()
		wait(5000)
		slave_control()
		wait(200)

main().mainloop()