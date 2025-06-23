

class Notification():

    def notify(self, *recipients):
        for recipient in recipients:
            print(f"Sending message to {recipient}")

class EmailNotification (Notification):
    def notify(self, recipient):
        print(f"Sending email to {recipient}")

class SMSNotification(Notification):
    def notify(self, recipient):
        print(f"Sending sms to {recipient}")