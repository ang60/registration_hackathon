from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'native_name',
            'phone_no',
            'gender',
            'date_of_birth',
            'team_name',
            'project_title',
            'github_repository',
            'programming_languages',
            'skill_level',
            'how_did_you_hear',
            'emergency_contact_name',
            'emergency_contact_relationship',
            'emergency_contact_phone',
            'terms_and_conditions_agreed',
            'consent_for_photos',
            'social_media_handles',
            'other_social_media',
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Customize the form if needed, for example, add CSS classes
        # to the fields or set placeholders.

    def clean_email(self):
        email = self.cleaned_data['email']
        # Your custom email validation logic
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Please use an email from example.com.')
        return email
    
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')

        if not date_of_birth:
            return date_of_birth

        input_formats = [
            '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y', '%B %d, %Y', '%d %B %Y'
        ]

        try:
            # Attempt to parse the date using the specified formats
            date_of_birth = forms.DateField(input_formats=input_formats).clean(date_of_birth)
        except forms.ValidationError:
            raise forms.ValidationError('Please enter a valid date of birth.')

        if date_of_birth.year < 1900:
            raise forms.ValidationError('Please enter a valid date of birth.')

        return date_of_birth


    def clean(self):
        cleaned_data = super().clean()
        # Add any additional validation or cleaning logic for the entire form here if needed
        return cleaned_data
