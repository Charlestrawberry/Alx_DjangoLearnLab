from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


def profile_upload_path(instance, filename):
    # e.g., media/profiles/user_12/filename.jpg
    return f'profiles/user_{instance.pk or "new"}/{filename}'

class CustomUserManager(UserManager):
    """
    Extends default UserManager so we can cleanly handle our extra fields.
    With AbstractUser, username remains the identifier unless you change USERNAME_FIELD.
    """

    def create_user(self, username, email=None, password=None, **extra_fields):
        # extra_fields may include date_of_birth, profile_photo
        return super().create_user(username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return super().create_superuser(username, email=email, password=password, **extra_fields)


class User(AbstractUser):
    """
    Custom user based on AbstractUser (keeps username, first_name, last_name, etc.)
    Adds:
      - date_of_birth (DateField)
      - profile_photo (ImageField)
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to=profile_upload_path, null=True, blank=True)

    # Keep username as the identifier (default). If you want email, change USERNAME_FIELD and REQUIRED_FIELDS.
    objects = CustomUserManager()

    def __str__(self):
        return self.username

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


    def __str__(self):
        return f"{self.title} by {self.author} {self.publication_year}"