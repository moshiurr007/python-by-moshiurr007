### python by moshiurr007 --> intermediate_level ###

# email simulator #

from datetime import datetime


class User:
    def __init__(self, name:str, email_address:str):
        self.name = name
        self.email_address = email_address
        self.inbox = Inbox()

    # send email
    def send_email(self, receiver, subject:str, body:str):
        if not isinstance(receiver, User):
            print("Invalid receiver.")
            return
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'\nEmail sent from {self.name} to {receiver.name} successfully.')

    # check inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.all_emails()

    # read an email
    def read_email(self, index:int):
        self.inbox.read_email(index=index)

    # delete an email
    def delete_email(self, index:int):
        self.inbox.delete_email(index=index)


class Email:
    def __init__(self, sender, receiver, subject:str, body:str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.now()
        self.read = False

    # mark as read
    def mark_as_read(self):
        self.read = True

    # display full email
    def display_full_email(self):
        self.mark_as_read()
        print('\n===== Email =====')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f"Received: {self.timestamp.strftime('%d %b, %Y - %H:%M')}")
        print(f'Subject: {self.subject}')
        print(f'Body: {self.body}')
        print('=================')

    def __str__(self):
        status = 'READ' if self.read else 'NEW'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | {self.timestamp.strftime('%d %b, %Y - %H:%M')}"


class Inbox:
    def __init__(self):
        self.emails = []

    # receive
    def receive_email(self, email):
        self.emails.append(email)

    # all emails
    def all_emails(self):
        if not self.emails:
            print("Empty Inbox.")
            return
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}: {email}")

    # read email
    def read_email(self, index:int):
        if not isinstance(index, int):
            print("Index must be an integer.")
            return
        if not self.emails:
            print("Empty Inbox.")
            return
        actual_index = index-1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email index.")
            return
        self.emails[actual_index].display_full_email()

    # delete email
    def delete_email(self, index:int):
        if not isinstance(index, int):
            print("Index must be an integer.")
            return
        if not self.emails:
            print("Empty Inbox.")
            return
        actual_index = index-1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email index.")
            return
        del self.emails[actual_index]
        print("Email deleted.")


def main():
    ali = User("Ali", "ali@email.com")
    hamza = User("Hamza", "hamza@email.com")
    sara = User("Sara", "sara@email.com")
    jamila = User("Jamila", "jamila@email.com")

    ali.send_email(hamza, "Lunch", "Biryani on Friday?")
    sara.send_email(hamza, "Greetings", "How are you doing, brother?")

    hamza.check_inbox()
    hamza.read_email(2)
    hamza.check_inbox()
    hamza.delete_email(2)
    hamza.check_inbox()

    hamza.send_email(sara, "Greetings", "I'm great. How are you, Sara?")
    jamila.send_email(sara, "College", "Will you go to college tomorrow?")

    sara.check_inbox()


if __name__ == '__main__':
    main()