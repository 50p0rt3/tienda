from django import forms

class FormContact(forms.Form):
    #Especificar los campor del formulario
    asunto=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField()