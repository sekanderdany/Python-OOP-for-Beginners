# Abstraction

class EmailService:
    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print(f"Sending email")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")


email = EmailService()
email.send_email()

# In this example, the `_connect`, `_authenticate`, and `_disconnect` methods are protected methods that are used internally by the `send_email` method. They are not intended to be accessed directly from outside the class, but they can be accessed by subclasses if needed.
