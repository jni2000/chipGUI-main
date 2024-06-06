from django import forms
class CreateNewList(forms.Form):
    nodeID = forms.CharField(label="Node ID", max_length=200)
    mtn = forms.CharField(label="MT#", max_length=200)