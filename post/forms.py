from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
	title = forms.CharField()
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell us more about Work/problem?'}), max_length=4000)


	class Meta:
		model = Post
		fields = ['title','description'] 

