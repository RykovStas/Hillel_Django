from django import forms


class Calc(forms.Form):
    a = forms.IntegerField(label='First cathet:', min_value=0)
    b = forms.IntegerField(label='Second cathet:', min_value=0)
