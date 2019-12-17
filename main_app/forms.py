from django.forms import ModelForm
from .models import Battles

class BattlesForm(ModelForm):
    class Meta:
        model = Battles
        fields = ['date', 'damage']