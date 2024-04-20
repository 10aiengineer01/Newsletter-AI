from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(grandparent_dir)

from agency import email, password

class SendNewsletterEmails(BaseTool):
    """
    Sends formatted newsletters to a list of subscribers.
    """

    def run(self) -> str:
        """
        Sends the newsletter emails to recipients.
        """
        image_paths = self.shared_state.get("image_paths")

        self.send_mail(image_paths)

        return "Newsletter is send successfully to the recipients."
    
    def send_mail(self, image_paths):
        content = self.shared_state.get("content")

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = f'Newsletter-Content: {content["TITLE"]}'

        html = f"""<html><head></head><body>
        <h1>{content["TITLE"]}</h1>
        <p>{content["INTRODUCTION"]}</p>
        """

        for i, (key, value) in enumerate(content["CONTENT"]):
            if key == 'subtitle':
                html += f"<h2>{value}</h2>"
            elif key == 'info':
                html += f"<p>{value}</p>"
            elif key == 'image':
                cid = os.path.basename(value)
                html += f'<p><img src="cid:{cid}"></p>'

        html += f"<p>{content['CONCLUSION']}</p></body></html>"
        msg.attach(MIMEText(html, 'html'))

        for image_path in image_paths:
            if os.path.isfile(image_path):
                cid = os.path.basename(image_path)
                with open(image_path, 'rb') as img:
                    mime_image = MIMEImage(img.read())
                    mime_image.add_header('Content-ID', f'<{cid}>')
                    msg.attach(mime_image)

        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
        server.quit()
