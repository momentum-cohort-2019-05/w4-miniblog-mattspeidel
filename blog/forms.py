from django import forms

class PostComment(forms.Form):
    commentpost = forms.TextInput()