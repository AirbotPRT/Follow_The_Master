import rospy
from std_msgs.msg import String

from drone_classes import drone

def get_info(drone):

	def callback(data):
		x=0
		y=0
		z=0
		o=0
		drone.update_data(x, y, z, o)


	rospy.init_node(drone.id +'_flight_info_listener',anonymous=True)

	rospy.Subscriber(drone.id+"/data/imu",String, callback)

#	try:

#	except rospy.ROSInterruptException:
#  		pass

	rospy.spin()

	def refresh_flight_info(drones):
		for drone in drones :
			get_info(drone)
		





  	