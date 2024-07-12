from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def enviar_email(para, assunto, corpo):
    host = "smtp.mail.yahoo.com"
    port = '587'
    login = "farias_ce@yahoo.com.br"
    senha = "xmnwyspwzueolomr"

    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)
        
        corpo_html = f"""
        <html>
        <body>
            <p>{corpo}</p>
        </body>
        </html>
        """

        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = para
        email_msg['Subject'] = assunto
        
        # Parte de texto em HTML
        email_msg.attach(MIMEText(corpo_html, 'html'))

        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso.")
        
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
