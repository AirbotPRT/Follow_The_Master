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
	def __init__():

	#Define function to take off
	def take_off():


	#Define function to land
	def land():



	#Define function to set which drone is the master
	def set_master(drone):




	#Define function to set the position of the slave, the same as the master
	def set_position(x,y,z,Orientation):



	#Define function to fix the slave altitude when master is moving
	def fix_altitude():



	#Define function to fix the slave distance when master is moving
	def fix_distance():



	#Define function to fix the slave orientation when master is moving
	def fix_orientation():

	#Define function to fix the slave direction when master is moving
	def fix_direction():







