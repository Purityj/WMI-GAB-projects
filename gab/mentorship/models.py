from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager

# define user roles
ROLE_CHOICES = [
    ('wmi_staff', 'Staff'),
    ('mentor', 'Mentor'),
    ('mentee', 'Mentee'),
]

class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser model"""
    
    def create_user(self, email, username, role, password: None, **extra_fields):
        # create and return a regular user
        # validate the role
        valid_roles = [choice[0] for choice in ROLE_CHOICES]
        if role not in valid_roles:
            raise ValueError(f"Invalid role: {role}. Must be one of: {valid_roles}")
        
        if not email:
            raise ValueError("The email field must be set")
        if not username:
            raise ValueError("The username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, role, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, role, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom user model."""

    # add role field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # override email field to make it required and unique
    email = models.EmailField(unique=True)

    # Use email as the primary identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']  # Username and role are required when creating a user

    objects = CustomUserManager()  # Use the custom manager

    def save(self, *args, **kwargs):
        # Ensure username is unique (already handled by AbstractUser, but for clarity)
        super().save(*args, **kwargs)

    def is_wmi_domain(self):
        """Check if the user's email domain matches wellsmountaininitiative.org."""
        domain = self.email.split('@')[-1]
        return domain == 'wellsmountaininitiative.org' or domain.endswith('.org')

    def __str__(self):
        return f"{self.username} ({self.email})"

