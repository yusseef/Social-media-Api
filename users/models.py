from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        new_user = self.model(email = email, **extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super User should have is_staff True"))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Super User should have is_superuser True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Super User should have is_active True"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    Gender_choices = [
        ('male', 'male'),
        ('female', 'female'),
        ]


    first_name = models.CharField(
        max_length = 50,
        unique = False,
        null = False,
        blank = False,
        verbose_name = _("First name"),
        help_text = _("Required / max-50 / letters, numbers, symbols and underscores")
        )
    
    last_name = models.CharField(
        max_length = 50,
        unique = False,
        null = False,
        blank = False,
        verbose_name = _("Last name"),
        help_text = _("Required / max-50 / letters, numbers, symbols and underscores")
        )

    email = models.EmailField(
        max_length = 200,
        unique = True,
        null = False,
        blank = False,
        verbose_name = _("Email"),
        help_text = _("Required / Follow email schema ex: john@doe.com")
    )
   
    gender = models.CharField(
        max_length = 50,
        choices = Gender_choices,
        verbose_name = _("Gender"),
        null = False,
        blank = False,
        help_text = _("Required / User's gender")
        )

    school = models.CharField(
        max_length = 255,
        unique = False,
        null = True,
        blank = True,
        verbose_name = _("School"),
    )

    street = models.CharField(
        max_length = 255,
        unique = False,
        null = True,
        blank = True,
        verbose_name = _("Street number"),
    )

    country = CountryField(blank_label = _("Country"))

    birthday = models.DateField(
        null = True,
        blank = True,
        verbose_name = _("Birthday date")
    )

    profile_pic = models.ImageField(
        upload_to = 'profile_image', 
        null = True, 
        blank = True,
        verbose_name = _("Profile picture"),
        )

    joining_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name = _("Joining date"),)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def address(self):
        return f"{self.street}, {self.country}"

    def __str__(self):
        return self.email