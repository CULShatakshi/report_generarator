from django.forms import ModelForm
from .models import Person
 
class PostForm(ModelForm):
    class Meta:
        model=Person
        fields = '__all__'

 