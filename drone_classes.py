#!/usr/bin/python

import abstractros
import math

class Drone(object):
    '''
        class Drone that represent a basic simplified drone.
        it suppose that the drone is under a perfect control loop
        the attributes only include x,y,z coordinates and the orientation
        The id correspond to the name given to the drone
    '''
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.z = 0
        self.o = 0

    @staticmethod
    def refresh_flight_info(drones):
        '''
            Static function to refresh the data
        '''
        for drone in drones:
            abstractros.get_info(drone)

    @staticmethod  
    def calc_distance(drone1, drone2):
        """
            function used to calculate the distance between two drones.
        """
        distance_x = drone1.x -drone2.x
        distance_y = drone1.y - drone2.y
        return math.sqrt(distance_x^2 + distance_y^2)

    @staticmethod 
    def calc_colinearity(drone1, drone2):
        """
            function used to calculate the colinearity error between drone1 and drone2 in deg.

            it represent the angle between drone 1 direction and drone 2.
        """
        p1x = drone1.x
        p1y = drone1.y
        p2x = drone1.x-Drone.calc_distance(drone1, drone2)*math.sin(drone1.o*2*math.pi/360)
        p2y = drone1.y-Drone.calc_distance(drone1, drone2)*math.cos(drone1.o*2*math.pi/360)
        p3x = drone2.x
        p3y = drone2.y

        p12 = math.sqrt((p1x - p2x)^2 + (p1y - p2y)^2)
        p13 = math.sqrt((p1x - p3x)^2 + (p1y - p3y)^2)
        p23 = math.sqrt((p2x - p3x)^2 + (p2y - p3y)^2)


        return (math.acos((p12**2 + p13**2 - p23**2) / (2 * p12 * p13)))*(360/(2*math.pi))    




class DroneSlave(Drone):
    """
     class drone slave herited from Drone
     has the ability to follow a master (defined as attribute)
    """
    def __init__(self,id):
        super(DroneSlave, self).__init__(id)
        self.master = None

    def take_off(self):
        """
            function to take off
        """
        abstractros.takeoff(self)

    def land(self):
        """
            function to land
        """
        abstractros.land(self)


    def goto(self, x, y, z, o):
        """
            function to go to the (x,y,z,o) point
        """
        abstractros.goto(self, x, y, z, o)


    #Define function to set which drone is the master
    def set_master(self, drone):
        """
            function to set the master
        """
        self.master = drone


    #Define function to fix the slave altitude when master is moving
    def fix_altitude(self, diff):
        """
            function to fix altitude difference between master and self
        """
        self.goto(self, self.x, self.y, self.master.z + diff, self.o)


    #Define function to fix the slave distance when master is moving
    def fix_distance(self, dist):
        """
            function to fix distance between master and self
        """
        p1x = self.x
        p1y = self.y
        p2x = self.x
        p2y = self.y+1
        p3x = self.master.x
        p3y = self.master.y

        p12 = math.sqrt((p1x - p2x)^2 + (p1y - p2y)^2)
        p13 = math.sqrt((p1x - p3x)^2 + (p1y - p3y)^2)
        p23 = math.sqrt((p2x - p3x)^2 + (p2y - p3y)^2)
        diff_angle = (math.acos((p12**2 + p13**2 - p23**2) / (2 * p12 * p13)))*(360/(2*math.pi))    

        x_target = self.x + (Drone.calc_distance(self.master, self)-dist)*math.cos(diff_angle*2*math.pi/360)
        y_target = self.y + (Drone.calc_distance(self.master, self)-dist)*math.sin(diff_angle*2*math.pi/360)

        self.goto(self, x_target, y_target, self.z, self.o)

    #Define function to fix the slave orientation when master is moving
    def fix_orientation(self, diff):
        """
            function to fix orientation difference between master and self
        """
        self.goto(self, self.x, self.y, self.z, self.master.o+diff)

    #Define function to fix the slave direction when master is moving
    def fix_colinearity(self, diff):
        """
            function to fix colinearity between master and self

            the diff arg correspond to the desired angle between the master direction and the slave
        """
        x_target = self.master.x-Drone.calc_distance(self.master, self)*math.sin((self.master.o+diff)*2*math.pi/360)
        y_target = self.master.y-Drone.calc_distance(self.master, self)*math.cos((self.master.o+diff)*2*math.pi/360)

        # would be better to impose a defined curve, but not possible actually.
        self.goto(self, x_target, y_target, self.z, self.o)







