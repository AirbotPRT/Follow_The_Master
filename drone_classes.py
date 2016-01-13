import abstractros

#Declare the data received from GPS on ROS network
class Drone:
	def __init__(self,id):

		
		self.id=id

	#adapter for data from ros
	def update_data(x,y,z,o):
		self.x=x
		self.y=y
		self.z=z
		self.o=o




class Drone_slave(Drone):
	def __init__(self):

	#Define function to take off
	def take_off(self):


	#Define function to land
	def land(self):



	#Define function to set which drone is the master
	def set_master(self,drone):




	#Define function to set the position of the slave, the same as the master
	def set_position(self,x,y,z,Orientation):



	#Define function to fix the slave altitude when master is moving
	def fix_altitude(self):


	#Define function to fix the slave distance when master is moving
	def fix_distance(self):



	#Define function to fix the slave orientation when master is moving
	def fix_orientation(self):

	#Define function to fix the slave direction when master is moving
	def fix_direction(sel)f:








