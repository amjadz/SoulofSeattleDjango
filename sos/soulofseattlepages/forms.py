from django import forms 
from bootstrap_datepicker_plus import DatePickerInput



class ContactToAddEventForm(forms.Form):
    event_name = forms.CharField(required=True)
    your_email = forms.EmailField(required=True)
    start_time = forms.CharField(required = True)
    end_time = forms.CharField(required = True)
    event_date = forms.DateField(required = True, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    message = forms.CharField(widget=forms.Textarea, required=True)