from django import forms
from .models import Warrior


class AddWarrior(forms.ModelForm):

    class Meta:
        model = Warrior

        fields = [
            'name',
            'race'
        ]
