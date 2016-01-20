#!/usr/bin/python

import rospy
import mavros
from geometry_msgs.msg import PoseWithCovarianceStamped

def get_info(drone):
    """
        Get flight info from ROS and insert it in the related drone object.

        It takes the information from ROS located at /{drone_id}/mavros/global_position/local,
        and select only the valuable data. Then it store it in the drone Object given in argument.

        :param drone: The drone from which coordinates will be updated
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """

    def callback(data):
        """
            callback function
        """
        drone.x = data.pose.pose.position.x
        drone.y = data.pose.pose.position.y
        drone.z = data.pose.pose.position.z
        drone.o = data.pose.pose.orientation.z*180 #en deg

    try:
        rospy.init_node('flight_info_listener', anonymous=True)

        rospy.Subscriber(drone.id+"/mavros/global_position/local", PoseWithCovarianceStamped, callback)

    except rospy.ROSInterruptException:
       print "oups :("

    rospy.spin()

def arm(drone):
    """
        Send a arm command to ROS for the drone send in param.

 
        :param drone: The drone that will takeoff
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """
    rospy.wait_for_service(drone.id+'/mavros/cmd/arming')
    try:
        print "ready"
        send_arm_command = rospy.ServiceProxy('arming', Arm)
        print "oklm"
        resp = send_arm_command('arg')
        return resp
    except rospy.ServiceException, ex:
        print "Service call failed: %s"%ex

def disarm(drone):
    """
        Send a disarm command to ROS for the drone send in param.
 
        :param drone: The drone that will takeoff
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """
    pass


def takeoff(drone):
    """
        Send a takeoff command to ROS for the drone send in param.
 
        :param drone: The drone that will takeoff
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """
    pass

def land(drone):
    
    """
        Send a land command to ROS for the drone send in param.
 
        :param drone: The drone that will land
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """
    pass

def goto(drone, x, y, z, o):
    """
        Send a goto command to ROS for the related drone .

        :param drone: The drone from which coordinates will be updated
        :param x: target point X coordinate
        :param y: target point Y coordinate
        :param z: target point Z coordinate
        :param o: target orientation between -1 and 1 (-1 = -180deg , 1 = 180deg)

        :type drone: Drone
        :type x: float
        :type y: float
        :type z: float
        :type o: float

        :return: Nothing
        :rtype: void
    """
    pass
