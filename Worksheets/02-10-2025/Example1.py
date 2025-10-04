# 1. Advanced Topic: Inheritance
# Inheritance allows a new class (child class or subclass) to adopt the attributes and
# methods of an existing class (parent class or superclass).
#
# Cybersecurity Application: Think of having a generic SecurityTool class that defines
# basic properties (like logging and connection methods). You can then create specialized tools
# like PortScanner or PacketSniffer that inherit those
# basics but add their own unique, specific functionality. This avoids redundant code.


class SecurityTool:
    """Base class for all security related tools."""

    def __init__(self,name,version="1.0"):
        self.name = name
        self.version = version
        self.is_running = False

    def start(self):
        """Standard method to start any tool."""
        print(f"[{self.name}] Starting Up...")
        self.is_running = True

    def log_action(self,action):
        """Standard method to logging action."""
        # This common method is inherited by all child classes.
        print(f"[{self.name}] Logging {action}...")


# Child Class (SubClass) - Inherits from SecurityTools

class PortScanner(SecurityTool):
    """A specialised tool for scanning ports, inheriting base methods."""

    # __init__ method overrides the parent's constructor but calls it first.
    def __init__(self, target_ip):
        # super() calls the parent class's __init__ method, ensuring
        # initialization of name, version, and is_running.
        super().__init__("NmapLiteScanner", "1.2")
        self.target_ip = target_ip
        self.open_ports = [] # Scanner-specific attribute

    def scan_port(self, port):
        """New, specialized method specific to the PortScanner."""
        if self.is_running:
            if port % 2 == 0:
                self.open_ports.append(port)
                # We use the inherited log_action method here!
                self.log_action(f"Port {port} is OPEN on {self.target_ip}")
            else:
                self.log_action(f"Port {port} is CLOSED")
        else:
            print(f"Tool must be started before scanning.")

# Instantiate and use
scanner = PortScanner("192.168.1.100")
scanner.start()  # Inherited from SecurityTool
scanner.scan_port(80)  # Scanner's specific method



