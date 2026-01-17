from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


# COMPLETE THIS CLASS
class NotificationFactory:
    @staticmethod
    def create_notification(type, recipient, sender, message):
        if type == NotificationType.EMAIL:
            return EmailNotification(recipient, sender, message)
        elif type == NotificationType.PUSH:
            return PushNotification(recipient, message)
        elif type == NotificationType.SMS:
            return SmsNotification(recipient, message)
        return None


# COMPLETE THIS CLASS
@dataclass
class Notification(ABC):
    @abstractmethod
    def send_notification(self):
        pass

    @abstractmethod
    def notification_type(self):
        pass


class NotificationType(Enum):
    EMAIL = "Email"
    PUSH = "Push"
    SMS = "SMS"


@dataclass
class EmailNotification(Notification):
    recipient: str
    sender: str
    message: str

    def send_notification(self):
        print(f"Email sent to {self.recipient} from {self.sender}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.EMAIL


@dataclass
class PushNotification:
    recipient: str
    message: str

    def send_notification(self):
        print(f"Push notification sent to device {self.recipient}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.PUSH


@dataclass
class SmsNotification:
    recipient: str
    message: str

    def send_notification(self):
        print(f"SMS sent to {self.recipient}")
        print(f"Message: {self.message}")

    def notification_type(self):
        return NotificationType.SMS
