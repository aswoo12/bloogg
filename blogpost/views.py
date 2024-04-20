from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .forms import CreatePostForm, UpdatePostForm
from .models import BlogPost

from django.contrib import messages



def home(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts }
    return render(request, 'blogpost/home.html', context=context)


def about(request):

  return render(request, 'blogpost/about.html')  # Replace 'about.html' with your actual template name



@login_required
def create_post_view(request):
    form = CreatePostForm()
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "The post has been created successfully.")
            return redirect("blog-home")
        else:
            messages.error(request, "Please correct the following errors:")
    else:
        form = CreatePostForm()
    context = {'form' : form }
    return render(request, 'blopost/create_post.html', context=context)


@login_required
def update_record_view(request, pk):
    posts = BlogPost.objects.get(id=pk) # get already ad data for update
    form = UpdatePostForm(instance=posts) # after getting data add into form
    
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=posts) # Update form with new submitted data
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Updated Successfully')
            return redirect("home")
        
    context = {'form' : form }
    return render(request, 'blopost/update_post.html', context=context)


@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {"post": post}
    return render(request, "blogpost/post_detail.html", context=context)
