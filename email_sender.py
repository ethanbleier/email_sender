# email_sender.py
from google.oauth2.service_account import Credentials
import email.message, gspread, smtplib

def send_emails(sheet_id, sender_email, sender_password):
    try:
        # Read textfile and assign to content
        with open('textfile.txt', 'r') as file:
            content = file.read()

        # Define scope & authorize credentials
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file('/Users/ethanbleier/onn/googstruct.json', scopes=scope)
        client = gspread.authorize(creds)

        # Open the Google Sheet and worksheet
        sheet = client.open_by_key(sheet_id).worksheet('a')

        # Read data from Google Sheet
        data = sheet.get_all_records()

        # "for each row in the google sheet":
        for row in data:
            # Read recipient email and first name from google sheet
            recipient_email = row['Email']
            recipient_name = row['First Name']

            # open and read subject txt
            with open('subject.txt', 'r') as g:
                subject = g.read()

            # Do templating and the encoding bug fix
            body_template = content.format(name=recipient_name)
            subject = subject.format(name=recipient_name)
            clean_body = body_template.replace('\xa0', ' ').encode()

            # Assemble email message
            msg = email.message.Message()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.set_payload(clean_body)

            # Connect to SMTP server and send email
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_email, sender_password)
            s.send_message(msg)
            s.quit()

        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
