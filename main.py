# main.py
import sys

# Check if Python 3 or a more recent version is required.
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMessageBox
from email_sender import send_emails

class EmailSenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Assigning sheet ID variable, sender email, and protected password
        self.sheet_id = '1oMJ-cRPvW48Wqee-67NpxzbvsB80CJrDliYGAWirTRw'
        self.sender_email = 'ebleier4@gmail.com'
        self.sender_password = 'jxzmdxyzyprwhrij'

    def initUI(self):
        self.setWindowTitle("Email Sender App")
        self.setGeometry(100, 100, 400, 250)

        # Text Field for Recipient's Email
        self.email_label = QLabel("Recipient's Email:")
        self.email_field = QLineEdit()
        
        # Text Field for Email Subject
        self.subject_label = QLabel("Email Subject:")
        self.subject_field = QLineEdit()

        # Send Email Button
        self.send_button = QPushButton("Send Email")
        self.send_button.clicked.connect(self.send_emails)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_field)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_field)
        layout.addWidget(self.send_button)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def send_emails(self):
        # Update textfile.txt with the entered text
        with open('textfile.txt', 'w') as file:
            file.write(self.email_field.text())

        # Update subject.txt with the entered subject
        with open('subject.txt', 'w') as file:
            file.write(self.subject_field.text())

        # Call email_sender.py to send emails
        if send_emails(self.sheet_id, self.sender_email, self.sender_password):
            self.show_success_message()
        else:
            self.show_error_message()

    def show_success_message(self):
        QMessageBox.information(self, "Success", "Emails sent successfully!")

    def show_error_message(self):
        QMessageBox.warning(self, "Error", "An error occurred while sending emails.")

def main():
    app = QApplication(sys.argv)

    # Load the external stylesheet
    with open('style.qss', 'r') as f:
        app.setStyleSheet(f.read())

    window = EmailSenderApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
