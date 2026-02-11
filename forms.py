from django import forms
from .models import Membership

class MembershipForm(forms.ModelForm):

    agree = forms.BooleanField(
        label='I Agree Terms',
        required=True
    )

    class Meta:
        model = Membership
        fields = ['name', 'email', 'phone', 'duration']

    # ===== Custom Validations =====

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits")

        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be 10 digits")

        return phone

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters")

        return name
