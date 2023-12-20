from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Accounts import views
from .forms import PostForm
from .models import Post


# Create your views here.
@login_required
def feed(request):
    print(request.user)
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')

    posts = Post.objects.order_by('-date_published')
    return render(request, 'feed.html', {'posts': posts, 'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect(views.home)
