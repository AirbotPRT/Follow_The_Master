#!/usr/bin/python

import abstractros

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




class DroneSlave(Drone):
    """
     class drone slave herited from Drone
     has the ability to follow a master (defined as attribute)
    """
    def __init__(self):
        super(DroneSlave, self).__init__()
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



    #Define function to set which drone is the master
    def set_master(self, drone):
        """
            function to set the master
        """
        self.master = drone


    #Define function to fix the slave altitude when master is moving
    def fix_altitude(self):
        """
            function to fix altitude difference between master and self
        """
        # TODO: code this
        pass

    #Define function to fix the slave distance when master is moving
    def fix_distance(self):
        """
            function to fix distance between master and self
        """
        # TODO: code this
        pass


    #Define function to fix the slave orientation when master is moving
    def fix_orientation(self):
        """
            function to fix orientation difference between master and self
        """
        # TODO: code this
        pass
    #Define function to fix the slave direction when master is moving
    def fix_colinearity(self):
        """
            function to fix colinearity between master and self
        """
        # TODO: code this
        pass







