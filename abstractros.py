#!/usr/bin/env python

import rospy
from mavros_msgs.srv import CommandBool, CommandTOL
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Point, Quaternion
from tf.transformations import quaternion_from_euler

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

    try:
        rospy.init_node('flight_info_listener', anonymous=True)
        print "waiting"
        data = rospy.wait_for_message(drone.id+"/mavros/global_position/local", PoseWithCovarianceStamped)
        print "youhou !"
        drone.x = data.pose.pose.position.x
        drone.y = data.pose.pose.position.y
        drone.z = data.pose.pose.position.z
        drone.o = data.pose.pose.orientation.z*180 #en deg

    except rospy.ROSInterruptException:
        print "oups :("



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
        send_arm_command = rospy.ServiceProxy(drone.id+'/mavros/cmd/arming', CommandBool)
        resp = send_arm_command(1)
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
    rospy.wait_for_service(drone.id+'/mavros/cmd/arming')
    try:
        send_arm_command = rospy.ServiceProxy(drone.id+'/mavros/cmd/arming', CommandBool)
        resp = send_arm_command(0)
        return resp
    except rospy.ServiceException, ex:
        print "Service call failed: %s"%ex


def takeoff(drone):
    """
        Send a takeoff command to ROS for the drone send in param.

        :param drone: The drone that will takeoff
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """
    min_pitch = 0.1
    yaw = drone.o
    latitude = drone.x
    longitude = drone.y
    altitude = drone.z + 2



    rospy.wait_for_service(drone.id+'/mavros/cmd/takeoff')
    try:
        send_takeoff_command = rospy.ServiceProxy(drone.id+'/mavros/cmd/takeoff', CommandTOL)
        resp = send_takeoff_command(min_pitch, yaw, latitude, longitude, altitude)
        return resp
    except rospy.ServiceException, ex:
        print "Service call failed: %s"%ex


def land(drone):

    """
        Send a land command to ROS for the drone send in param.

        :param drone: The drone that will land
        :type drone: Drone
        :return: Nothing
        :rtype: void
    """
    min_pitch = 0.0
    yaw = drone.o
    latitude = drone.x
    longitude = drone.y
    altitude = 0


    rospy.wait_for_service(drone.id+'/mavros/cmd/land')
    try:
        send_land_command = rospy.ServiceProxy(drone.id+'/mavros/cmd/land', CommandTOL)
        resp = send_land_command(min_pitch, yaw, latitude, longitude, altitude)
        return resp
    except rospy.ServiceException, ex:
        print "Service call failed: %s"%ex


def goto(drone, posx, posy, posz, poso):
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
    target_pos = PoseStamped(header=Header(frame_id='mavsetpos', stamp=rospy.get_rostime()))
    target_pos.pose.position = Point(x=posx, y=posy, z=posz)

    quat = quaternion_from_euler(0, 0, poso/180)
    target_pos.pose.orientation = Quaternion(*quat)


    pub = rospy.Publisher(drone.id+"/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    pub.publish(target_pos)
