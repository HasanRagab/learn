from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        """Receive an update from the subject."""
        pass

class EmailSubscriber(Observer):
    def __init__(self, email):
        self.email = email

    def update(self, message: str):
        print(f"📧 Email sent to {self.email}: {message}")

class SMSSubscriber(Observer):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, message: str):
        print(f"📱 SMS sent to {self.phone_number}: {message}")

class PushNotificationSubscriber(Observer):
    def __init__(self, username):
        self.username = username

    def update(self, message: str):
        print(f"🔔 Push notification for {self.username}: {message}")


class Subject:
    def __init__(self):
        self._observers = []  

    def attach(self, observer: Observer):
        """Attach an observer."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Detach an observer."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        """Notify all observers about an event."""
        for observer in self._observers:
            observer.update(message)


news_channel = Subject()
email_subscriber = EmailSubscriber("user@example.com")
sms_subscriber = SMSSubscriber("+1234567890")
push_subscriber = PushNotificationSubscriber("JohnDoe")

news_channel.attach(email_subscriber)
news_channel.attach(sms_subscriber)
news_channel.attach(push_subscriber)

news_channel.notify("🔥 Breaking News: Python Observer Pattern in Action!")

news_channel.detach(sms_subscriber)


news_channel.notify("📢 Another Update: Observer Pattern is Powerful!")
