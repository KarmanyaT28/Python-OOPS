# 2. Advanced Topic: Polymorphism
# Polymorphism (meaning "many forms") is the concept that different classes can be
# treated uniformly, even if they have different underlying implementations.
# The most common form is Method Overriding.
#
# Method Overriding: A subclass provides a specific implementation for a method that is
# already defined in its superclass.
#
# Cybersecurity Application: If you have several security devices (Firewall, IDS, Router), they all need a block() method. However, a Firewall blocks by updating its rule set, while an IDS blocks by sending a kill signal. Polymorphism
# allows you to call device.block() on any object, and the correct, specialized code runs automatically.
#

# Base class
class SecurityDevice:
    def __init__(self, device_id):
        self.device_id = device_id

    def block_ip(self, ip_address):
        """Default (generic) block method - should be overridden."""
        print(f"Device {self.device_id}: Blocking IP {ip_address} using standard procedure.")


# Subclass 1: Firewall Implementation
class Firewall(SecurityDevice):

    def block_ip(self, ip_address):
        """Overridden method: Blocks by adding a rule (Firewall's specific behavior)."""
        # This replaces the generic method from the parent class
        print(f"FIREWALL {self.device_id}: ADDING DENY RULE for {ip_address} to chain.")


# Subclass 2: IDS Implementation
class IDS(SecurityDevice):

    def block_ip(self, ip_address):
        """Overridden method: Blocks by session termination (IDS's specific behavior)."""
        print(f"IDS {self.device_id}: TERMINATING ALL SESSIONS associated with {ip_address}.")


# Polymorphic Usage: Treating objects of different types the same way
devices = [Firewall("FW-01"), IDS("SNORT-05")]
ip_to_block = "172.16.1.50"

for device in devices:
    # We call the same method (block_ip), but due to polymorphism,
    # the correct, specialized version runs for each object.
    device.block_ip(ip_to_block)
