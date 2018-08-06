from django import forms

class AddDetails(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    dish=forms.CharField()
    phno=forms.IntegerField()

class DispDetails(forms.Form):
    name=forms.CharField()