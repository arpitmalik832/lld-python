import threading
from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self):
        NotificationService.get_instance().add_observer(self)

    @abstractmethod
    def send_notification(self, message: str):
        pass


class Publisher(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self, message: str):
        pass


class EmailService(Observer):
    def send_notification(self, message: str):
        print(f"Printing Email Notification: {message}")


class AppService(Observer):
    def send_notification(self, message: str):
        print(f"Printing App Notification: {message}")


class SMSService(Observer):
    def send_notification(self, message: str):
        print(f"Printing SMS Notification: {message}")


class NotificationService(Publisher):
    __instance: "NotificationService" = None
    __lock = threading.Lock()

    @staticmethod
    def get_instance() -> "NotificationService":
        if NotificationService.__instance is None:
            with NotificationService.__lock:
                if NotificationService.__instance is None:
                    NotificationService.__instance = NotificationService()
        return NotificationService.__instance

    def __init__(self):
        self.observers = []

    def update_notifications(self, message: str):
        self.notify_observers(message)

    def notify_observers(self, message: str):
        for observer in self.observers:
            observer.send_notification(message)

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)


def main():
    email_service = EmailService()
    app_service = AppService()
    sms_service = SMSService()
    notification_service = NotificationService.get_instance()
    notification_service.update_notifications("Hello World")


main()
