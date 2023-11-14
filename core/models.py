from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    native_name = models.CharField(max_length=50)  # Adjust the max length as needed
    phone_no = models.CharField(max_length=15)  # Adjust the max length as needed
    gender = models.CharField(max_length=10, choices=(
        ('' ,'select gender'),
        ('male', 'Male'),
        ('female', 'Female'),
    ), default='')
    date_of_birth = models.DateField(null=False, blank=False)
    # Additional fields based on earlier suggestions
    team_name = models.CharField(max_length=100, blank=True, null=True)
    project_title = models.CharField(max_length=255, blank=True, null=True)
    github_repository = models.URLField(max_length=200, blank=True, null=True)
    programming_languages = models.CharField(max_length=255, blank=True, null=True)
    skill_level = models.CharField(max_length=20, choices=(
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ), default='beginner')

    how_did_you_hear = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    terms_and_conditions_agreed = models.BooleanField(default=False)
    consent_for_photos = models.BooleanField(default=False)
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('website', 'Website'),
        ('other','other'),
        # Add other social media platforms as needed
    ]

    social_media_handles = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=SOCIAL_MEDIA_CHOICES,
        help_text="Select one or more social media platforms.",
    )
    other_social_media = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'native_name', 'phone_no', 'gender', 'date_of_birth']

    def __str__(self):
        return "{} - {}".format(self.username, self.email)

    
    
