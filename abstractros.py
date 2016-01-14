import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def get_info(drone):

    def callback(data):
        print data.pose.pose.position.x
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        z = data.pose.pose.position.z
        o = data.pose.pose.orientation.z
        drone.update_data(x, y, z, o)

    try:
        rospy.init_node('flight_info_listener', anonymous=True)

        rospy.Subscriber(drone.id+"/global_position/local", PoseWithCovarianceStamped, callback)

    except rospy.ROSInterruptException:
       print "oups :("

    rospy.spin()
       





    