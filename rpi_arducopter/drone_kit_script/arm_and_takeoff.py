from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
#import exceptions
import math
import argparse
import dronekit

def connectMycopter():
    # parser = argparse.ArgumentParser(description='commands')
    # parser.add_argument('--connect')
    # args = parser.parse_args()
    
    # connection_string = args.connect
    # baud_rate = 115200
    
    vehicle = dronekit.connect(ip="/dev/ttyAMA0", baud=115200, wait_ready=True)
    #vehicle = dronekit.connect(ip="/dev/ttyAMA0", baud=57600, wait_ready=True)
    print(vehicle.mode.name)
    
    #vehicle = connect(connection_string, baud=baud_rate,wait_ready=True)
    return vehicle

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

        
    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    #vehicle.mode = VehicleMode("GUIDED")

    vehicle.armed = True

    while not vehicle.armed:      
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command 
    #  after Vehicle.simple_takeoff will execute immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)      
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: #Trigger just below target alt.
            print("Reached target altitude")
            break
        time.sleep(1)


vehicle = connectMycopter()
arm_and_takeoff(1)
print("End of Flight...")

#Arm and take of to altitude of 5 meters
