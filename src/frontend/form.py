from django import forms
from .models import Enter_Url
   
# create a ModelForm
class UrlForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Enter_Url
        fields = "__all__"