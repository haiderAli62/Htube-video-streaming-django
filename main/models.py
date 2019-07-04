from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User


class Video(models.Model):
	video_title = models.CharField(max_length=250)
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	description = models.TextField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	upload_date = models.DateTimeField(default=timezone.now)
	videos = models.FileField(upload_to='videos/' , null=True)
	ratedUsers = models.ManyToManyField(User, blank = True, related_name='ratedUsersVideo' )

class Comment(models.Model):
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	video = models.ForeignKey(Video , on_delete=models.CASCADE , related_name="comments")
	comment = models.TextField()
	comment_date = models.DateTimeField(default=timezone.now)




