from django import forms
from .models import Netbox

class NetboxForm(forms.ModelForm):
    class Meta:
        model = Netbox
        fields = ['hostname', 'username', 'pod_count']  
