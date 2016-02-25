from django import forms
from .models import FeatureRequest, Client

class FeatureRequestForm(forms.ModelForm):
    """Feature Request form"""
    class Meta:
            model = FeatureRequest
            fields = ['title','description','client','priority','target_date','url','product_area']
            widgets = {
               'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Title'
                }),
               'description': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Description'
                }),
               'client': forms.Select(attrs={
                    'class': 'form-control'
                }),
               'priority': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'Priority'
                }),
               'target_date': forms.DateInput(attrs={
                    'class': 'form-control',
                    'id': 'flatpickr',
                    'placeholder':'YYYY-MM-DD'
                }),
               'url': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder':'URL'
                }),
               'product_area': forms.Select(attrs={
                    'class': 'form-control'
                })
            }


class ClientForm(forms.ModelForm):
    """Client form"""
    class Meta:
        model = Client
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',    
                }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',    
                }),
        }

    