from django import forms 


class ContactToAddEventForm(forms.Form):
    event_name = forms.CharField(required=True)
    your_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)