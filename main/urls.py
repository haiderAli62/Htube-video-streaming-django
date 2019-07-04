from django.urls import path
from . import views 
urlpatterns = [
	path("uploadVideo" , views.upload_view , name="upload"),
	path("" , views.index , name="index" ),
	path("video_details/<pk>",views.video_detail_view ,name="video_details"),
	path('like_video/<int:video_id>', views.LikeVideo, name='like_video'),
    path('dislike_video/<int:video_id>', views.DislikeVideo, name = 'dislike_video')


]