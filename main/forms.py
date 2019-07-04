from django import forms
from main.models import Video , Comment
class VideoForm(forms.Form):
	title = forms.CharField(max_length=250)
	description = forms.CharField(widget=forms.Textarea)
	video = forms.FileField()
	class Meta:
		model = Video

class CommentForm(forms.Form):
	comment_desc = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Comment


