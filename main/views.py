from django.shortcuts import render , get_object_or_404
from .forms import VideoForm , CommentForm
from django.shortcuts import redirect
from .models import Video , Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def upload_view(request):
	if request.method == "POST":
	    form = VideoForm(request.POST , request.FILES)
	    if form.is_valid():
	    	video_obj = Video()
	    	video_obj.video_title = form.cleaned_data['title']
	    	video_obj.description = form.cleaned_data['description']
	    	video_obj.videos = form.cleaned_data['video']
	    	video_obj.user = request.user
	    	video_obj.save()
	    	return HttpResponseRedirect(reverse("index"))

	else:
		form = VideoForm()
	return render(request , "main/upload.html",{"form":form})

	

def index(request):
	if not request.user.is_authenticated:
		return render(request , "login/login.html" )
	add = Video.objects.order_by('-upload_date')
	print("mian app")
	current_user = request.user    # currently logged in usesr
	print(current_user.username)
	return render(request , "login/index.html" , {"add":add ,"user": current_user })

def video_detail_view(request , pk):
	details = Video.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment_obj = Comment()
			comment_obj.user = request.user
			comment_obj.video = details
			comment_obj.comment = form.cleaned_data['comment_desc']
			comment_obj.save()
			return redirect("video_details" , pk=details.pk)
	else:
		form = CommentForm()
	is_liked = False
	video_comments = details.comments.all()
	return render(request , "main/videoDetails.html" , {"is_liked":is_liked,"details" : details , "form":form,"comments":video_comments})

@login_required
def LikeVideo(request,video_id):
    video = get_object_or_404(Video, pk = video_id)
    hasRated = False
    for rateduser in video.ratedUsers.all():
        if rateduser.username == request.user.username:
            hasRated = True
            break
    if hasRated == False:
        video.likes = video.likes + 1
        video.ratedUsers.add(request.user)
        video.save()
    else:
        print("HAS ALREADY VOTED!")

    return redirect('/video_details/'+str(video_id))

@login_required
def DislikeVideo(request,video_id):
    video = get_object_or_404(Video, pk = video_id)
    hasRated = False
    for rateduser in video.ratedUsers.all():
        if rateduser.username == request.user.username:
            hasRated = True
            break
    if hasRated == False:
        video.dislikes = video.dislikes + 1
        video.ratedUsers.add(request.user)
        video.save()
    else:
        print("HAS ALREADY VOTED!")

    return redirect('/video_details/'+str(video_id))
