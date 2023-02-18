from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import math
import argparse

def connectMycopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()
    
    connection_string = args.connect
    baud_rate = 115200
    
    vehicle = connect(connection_string, baud=baud_rate,wait_ready=True)
    return vehicle


def arm():
    #while vehicle.is_armable==False:
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable...")
        time.sleep(1)
        
    print("Yoo vehicle is now armable...")
    print("")
    
    vehicle.armed=True
    
    #while vehicle.armed==False:
    while not vehicle.armed:
        print("Waiting for drone to become armed...")
        time.sleep(1)
        
    print("Vehicle is now armed...")
    return None


vehicle = connectMycopter()
arm()
print("End of Flight...")

