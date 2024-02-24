from django import forms
from .models import TimFerrissPodcast

class TimFerrissForm(forms.ModelForm):
      class Meta:
            model = TimFerrissPodcast
            fields = "__all__"