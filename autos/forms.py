from autos.models import Make
from django.forms import ModelForm

class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = "__all__"