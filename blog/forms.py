from django import forms

from .models import Post, Cv

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'intro', 'image1', 'image2')

class CvForm(forms.ModelForm):

	class Meta:
		model = Cv
		fields = ('name', 'phone_number', 'email', 'intro', 'education', 'experience', 'skills', 'interests')