import dronekit
vehicle = dronekit.connect(ip="/dev/ttyAMA0", baud=115200, wait_ready=True)
#vehicle = dronekit.connect(ip="/dev/ttyAMA0", baud=57600, wait_ready=True)
print(vehicle.mode.name)
