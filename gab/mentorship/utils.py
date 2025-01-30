
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

def send_login_email(user_email, role):
    # generate a temporary password
    temp_password = get_random_string(8)

    # get the CustomUser model
    User = get_user_model()  #dynamically fetches CustomUser instead of default User
    user = User.objects.get(email=user_email)
    username = user.username

    # set the temporary password 
    user.set_password(temp_password)
    user.save()

    # prepare the email content
    subject = "Login to Access Mentorship Resources"
    message = f"""
Dear {username},

Welcome to the Scholars Mentorship Program resources portal!

To access our mentorship resources, please follow these steps:

1. Visit: https://wmi-gab-project.vercel.app/login/
2. Log in using the following credentials:
   • Email: {user_email}
   • Password: {temp_password}

📌 Available Materials for mentees on Academic Track: Only Sessions 1 & 2 materials are available on the website. Use these to get started as we add the remaining sessions soon.

If you encounter any issues accessing the platform, please contact our support team at scholarmentorship@wellsmountaininitiative.org.

Best regards,
Purity Jangaya
Scholars Mentorship Program Coordinator

    """
    from_email = 'noreply.scholarmentorship@gmail.com'  # replace with sender email
    recipient_list = [user_email]

    # send the email
    send_mail(subject, message, from_email, recipient_list)
