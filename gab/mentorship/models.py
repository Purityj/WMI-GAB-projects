from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# define user roles
ROLE_CHOICES = [
    ('wmi_staff', 'Staff'),
    ('mentor', 'Mentor'),
    ('mentee', 'Mentee'),
]

class CustomUser(AbstractUser):
    # add role field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # related name fixes to avoid clashes
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    # override email field to make it required and unique
    email = models.EmailField(unique=True)

     # ensure email is the username for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']  # Username is still required for Django but not used to log in

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email    #autopopulate username with email
        super().save(*args, **kwargs)

    def is_wmi_domain(self):
        """check if the user's email domain matches wellsmountaininitiative.org"""
        domain = self.email.split('@')[-1]
        return domain == 'wellsmountaininitiative.org' or domain.endswith('.org')

    def __str__(self):
        return self.email
