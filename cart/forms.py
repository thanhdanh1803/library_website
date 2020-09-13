from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime, timedelta

LOAN_DURATION = [(i, str(i)) for i in range(1, 5)]
class BookOrderForm(forms.Form):
    start_date = str(datetime.now().date())
    stop_date = datetime.now() + timedelta(days=30)  
    stop_date = str(stop_date.date())
    due_date = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y', options={'minDate':start_date, 'maxDate':stop_date}),label='')
    update = forms.BooleanField(required=False, widget=forms.HiddenInput)