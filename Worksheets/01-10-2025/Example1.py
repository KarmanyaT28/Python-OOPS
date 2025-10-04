# Modelling Network Assets - Classes & Objects

#
# Core Topic: Classes and Objects
# A class is a blueprint for creating objects. Think of a class like
# the schematic for a networking device. The class defines what properties (attributes)
# and actions (methods) all devices of that type will have. An object is a specific
# instance of that class—an actual firewall or router created from the schematic
#

class NetworkDevice:
    # Class Attribute : Shared by all instances
    OS_TYPE = 'Linux'

    def __init__(self,ip_address,device_type):
        self.ip_address = ip_address
        self.device_type = device_type
        self.is_active = True
        print(f"Device {self.ip_address} ({self.device_type}) created")


    def ping(self,target_ip):
        """An instance method simulating a network check"""

        if self.is_active:
            print(f"{self.ip_address} is pinging {target_ip}...")
            return True

        else:
            print(f"{self.device_type} is offline")
            return False


    def disable(self):
        """A method to change the state of the device"""
        self.is_active = False
        print(f"Device {self.ip_address} has been disabled")



# Creating Objects (instantiation)

router = NetworkDevice('10.0.0.1','Router')
firewall = NetworkDevice('10.0.0.2','Firewall')


# Calling methods
router.ping("8.8.8.8")
firewall.disable()
firewall.ping("192.168.1.1")

# Accessing attributes
print(f"Router OS: {router.OS_TYPE}")




