
# forms.py 
from django import forms 
from api.models import ReviewsPictures
  
class PictureForm(forms.ModelForm): 
    class Meta: 
        model = ReviewsPictures 
        fields = ['id','picture'] 