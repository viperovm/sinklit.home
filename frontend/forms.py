from django import forms


class MainForm(forms.Form):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Ваш телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш email', widget=forms.TextInput(attrs={'class': 'form-control'}))
