from django import forms
import datetime


class RegistrationForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=32, widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "Enter name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "user@mail.com",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))

    # def clean_email(self):
    #     email: str = self.cleaned_data["email"]
    #     if not (email.endswith("vk.team") or email.endswith("corp.mail.ru")):
    #         raise forms.ValidationError("Use corporate email")
    #     return email

class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))

    # def clean_email(self):
    #     email: str = self.cleaned_data["email"]
    #     if not (email.endswith("vk.team") or email.endswith("corp.mail.ru")):
    #         raise forms.ValidationError("Use corporate email")
    #     return email


class ImageForm(forms.Form):
    image = forms.ImageField()


class ManyFieldsForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    email = forms.EmailField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.datetime.today)
    sex = forms.ChoiceField(choices=[("M", "Mail"), ("F", "Female")])


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "user@mail.com",
    }))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        "class": "form-check-input",
    }))
    birthdate = forms.DateField(initial=datetime.datetime.today, widget=forms.DateInput(attrs={
        "class": "form-control",
        "type": "date",
    }))
    sex = forms.ChoiceField(choices=[("M", "Mail"), ("F", "Female")], widget=forms.RadioSelect(attrs={
        "class": "form-check-inline",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
    }))
