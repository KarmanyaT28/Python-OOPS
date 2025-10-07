# 1. Advanced Topic: Abstract Base Classes (ABCs)️
# Abstract Base Classes (ABCs) are essential for defining a blueprint or contract
# that must be followed by any class that inherits from it. They enforce that subclasses
# implement specific methods.
#
# Why it matters for Cybersecurity: When designing a framework (like a system for
# handling alerts), you want to guarantee that every new component (e.g., an email alerter,
# a Slack alerter, a database logger)
# has a required send_alert() method. ABCs prevent developers from creating incomplete or broken components.
#
# To use ABCs in Python, we import the ABC class and
# the @abstractmethod decorator from the abc module.

from abc import ABC, abstractmethod


# The Parent class is abstract and cannot be instantiated directly
class AlertSystem(ABC):
    """
    Abstract Base Class for all alert mechanisms.
    It mandates a 'send_alert' method.
    """

    def __init__(self, severity):
        self.severity = severity

    @abstractmethod
    def send_alert(self, message):
        """This method MUST be implemented by all subclasses."""
        pass  # The 'pass' keyword here signals the method is abstract

    def log_status(self):
        """This is a concrete (non-abstract) method inherited normally."""
        print(f"[{self.severity}] Alert status checked.")


# Subclass 1: Must implement send_alert()
class EmailAlerter(AlertSystem):

    def __init__(self, recipient, severity="Medium"):
        super().__init__(severity)
        self.recipient = recipient

    # Implementing the abstract method is mandatory
    def send_alert(self, message):
        print(f"EMAIL ALERT to {self.recipient}: {self.severity} - {message}")


# Subclass 2: Must implement send_alert()
class SlackAlerter(AlertSystem):

    def send_alert(self, message):
        # Implementing the abstract method
        print(f"SLACK Webhook: Posting {self.severity} notification: {message}")


# Usage
email = EmailAlerter("security@corp.com")
email.send_alert("Unauthorized connection attempt.")
email.log_status()