from django import forms

LOAN_DURATION = [(i, str(i)) for i in range(1, 5)]
class BookOrderForm(forms.Form):
    duration = forms.TypedChoiceField(label='Thời gian mượn', choices=LOAN_DURATION, coerce=int)
    update = forms.BooleanField(required=False, widget=forms.HiddenInput)