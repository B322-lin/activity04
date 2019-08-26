from django import forms
from .models import Status, Department, Club, Income


class SearchForm(forms.Form):

    status = forms.ModelChoiceField(
        queryset=Status.objects, label='キャリアレベル', required=False)

    department = forms.ModelChoiceField(
        queryset=Department.objects, label='部署', required=False)

    club = forms.ModelChoiceField(
        queryset=Club.objects, label='部活', required=False)

    income = forms.ModelChoiceField(
        queryset=Income.objects, label='年収', required=False)