import abstractros

#Declare the data received from GPS on ROS network
class Drone(object):
	def __init__(self,id):
		self.id=id
		self.x=0
		self.y=0
		self.z=0
		self.o=0

	@staticmethod
	def refresh_flight_info(drones):
  	  for drone in drones:
   	     get_info(drone)




class Drone_slave(Drone):
	def __init__(self):
		super(Drone_slave, self).__init__()
		self.master=None

	#Define function to take off
	def take_off(self):
		abstractros.takeOff()

	#Define function to land
	def land(self):
		abstractros.land()



	#Define function to set which drone is the master
	def set_master(self,drone):
		self.master=drone



	#Define function to fix the slave altitude when master is moving
	def fix_altitude(self):
		pass

	#Define function to fix the slave distance when master is moving
	def fix_distance(self):
		pass


	#Define function to fix the slave orientation when master is moving
	def fix_orientation(self):
		pass
	#Define function to fix the slave direction when master is moving
	def fix_direction(self):
		pass







