from django import forms

from . import models


class SaveForm(forms.ModelForm):
    class Meta:
        fields = ("title","url")
        model = models.Random_Link

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(SaveForm, self).__init__(*args, **kwargs)
