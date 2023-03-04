from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        
class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('location', 'price', 'area', 'bedrooms', 'bathrooms', 'stories',
                  'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
                  'parking', 'prefarea', 'furnishingstatus')
