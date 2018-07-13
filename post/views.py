from django.shortcuts import render
from .models import Post
from .forms import NewPostForm
from django.contrib.auth.models import User

def home(request):
	posts = Post.objects.all()
	return render(request, 'home.html', {'posts' : posts})

def show_topics(request,pk):
	topic = Post.objects.get(pk=pk)
	return render(request,'topics.html', {'topic': topic}) 
    

def post_topics(request):
    user = User.objects.first() # get the currently logged in users
    if request.method == 'POST':
    	form = NewPostForm(request.POST) #send the data to server
    	if form.is_valid():
    		form.save()           #incomplete form view
    		post = Post.objects.create(
                 title = form.cleaned_data.get('title'),
                 description = form.cleaned_data.get('description'),
                 created_by = user
    			)
    		return redirect('home') # TODO: redirect to the home page
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form': form}) 
