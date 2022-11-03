from time import sleep

from django import forms
from django.core.mail import send_mail
from .tasks import send_email_feedback


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        send_email_feedback.delay(self.cleaned_data['email'],self.cleaned_data['message'])
