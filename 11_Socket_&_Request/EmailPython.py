# Python code to illustrate Sending mail from your Gmail account
import smtplib

# creates SMTP session
session_Obj = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
session_Obj.starttls()

# Authentication
sender_email_id = "tanvirah1172@gmail.com"
sender_email_id_password = "TalGaseVut4U"
session_Obj.login(sender_email_id, sender_email_id_password)

# message to be sent
message = "python says you hello!"

# sending the mail
receiver_email_id = "tanvirah325@gmail.com"
session_Obj.sendmail(sender_email_id, receiver_email_id, message)

# terminating the session
session_Obj.quit()