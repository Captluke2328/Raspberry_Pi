from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import exceptions
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
    if not vehicle.is_armable:
        if not vehicle.mode.name == "STABILIZE":
            vehicle.mode = VehicleMode("STABILIZE")
            while not vehicle.mode.name == "STABILIZE":
                print("waiting for mode change...")
                time.sleep(1)
     
    while not vehicle.is_armable:
        print("waiting for vehicle to initialize...")
        time.sleep(1)
    print("Vehicle is ready to go")
    vehicle.armed=True

    #while not vehicle.mode.name == "STABILIZE":
    #    print("Waiting for vehicle to become armable...")
    #    time.sleep(1)
    #while vehicle.is_armable==False:
    #    print("Waiting for vehicle to become armable...")
    #    time.sleep(1)
        
    #print("Yoo vehicle is now armable...")
    #print("")
    
    #vehicle.armed=True
    
    #while not vehicle.mode.name == "STABILIZE":
    #while vehicle.armed==False:
    #    print("Waiting for drone to become armed...")
    #    time.sleep(1)
        
    #print("Vehicle is now armed...")
    return None


vehicle = connectMycopter()
arm()
print("End of Flight...")


