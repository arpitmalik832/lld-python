from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class NotificationType(Enum):
    EMAIL = 1
    PUSH = 2


@dataclass
class NotificationTemplate(ABC):
    message: str

    @abstractmethod
    def apply_template(self) -> str:
        pass

    @abstractmethod
    def notification_type(self) -> NotificationType:
        pass


@dataclass
class Notification(ABC):
    recipient: str
    template: NotificationTemplate

    @abstractmethod
    def notification_type(self) -> NotificationType:
        pass

    @abstractmethod
    def send_notification(self):
        pass


class NotificationSender(ABC):
    def __init__(self, notification: Notification):
        self.notification = notification

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def notification_type(self):
        pass


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self, recipient: str, template: NotificationTemplate):
        pass

    @abstractmethod
    def create_template(self, message: str):
        pass

    @abstractmethod
    def create_sender(self, notification: Notification):
        pass


class EmailNotificationFactory(NotificationFactory):
    def create_notification(
        self, recipient: str, template: NotificationTemplate, sender: str = ""
    ):
        return EmailNotification(recipient, template, sender)

    def create_template(self, message: str):
        return EmailNotificationTemplate(message)

    def create_sender(self, notification: Notification):
        return EmailNotificationSender(notification)


class PushNotificationFactory(NotificationFactory):
    def create_notification(self, recipient: str, template: NotificationTemplate):
        return PushNotification(recipient, template)

    def create_template(self, message: str):
        return PushNotificationTemplate(message)

    def create_sender(self, notification: Notification):
        return PushNotificationSender(notification)


@dataclass
class EmailNotification(Notification):
    sender: str

    def notification_type(self) -> NotificationType:
        return NotificationType.EMAIL

    def send_notification(self):
        # Logic to send an email
        print(f"Email sent to {self.recipient} from {self.sender}")
        print("Message:", self.template.message)


@dataclass
class PushNotification(Notification):
    def notification_type(self) -> NotificationType:
        return NotificationType.PUSH

    def send_notification(self):
        # Logic to send a push notification
        print(f"Push notification sent to device {self.recipient}")
        print("Message:", self.template.message)


class EmailNotificationSender(NotificationSender):
    def __init__(self, notification: Notification):
        super().__init__(notification)

    def send(self):
        print(f"Sending Email notification to {self.notification.recipient}")

    def notification_type(self):
        return NotificationType.EMAIL


class PushNotificationSender(NotificationSender):
    def __init__(self, notification: Notification):
        super().__init__(notification)

    def send(self):
        print(f"Sending Push notification to {self.notification.recipient}")

    def notification_type(self):
        return NotificationType.PUSH


@dataclass
class PushNotificationTemplate(NotificationTemplate):
    def apply_template(self) -> str:
        print("Applying Push notification template")
        return self.message

    def notification_type(self) -> NotificationType:
        return NotificationType.PUSH


@dataclass
class EmailNotificationTemplate(NotificationTemplate):
    def apply_template(self) -> str:
        print("Applying Email notification template")
        return self.message

    def notification_type(self) -> NotificationType:
        return NotificationType.EMAIL
