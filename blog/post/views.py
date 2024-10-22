from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auther = request.user
            instance.save()
            return redirect('/')
    else:
        form = PostForm()

    context = {
        'posts':posts,
        'form':form,
    }
    return render(request, 'post/home.html', context)

@login_required(login_url='login')
def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.all()
    total_comments = comments.count()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            
            instance.save()
            return redirect('detail', pk=post.id)
    else:
        form = CommentForm()

    context = {
        'post' : post,
        'form': form,
        'comments':comments,
        'total_comments': total_comments,
    }
    return render(request, 'post/post_detail.html', context)

@login_required(login_url='login')
def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=post.id)
    else:
        form = PostForm(instance=post)

    context = {
        'form':form,
    }
    return render(request, 'post/update_post.html', context)

@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    
    context = {
        'post':post,
    }
    return render(request, 'post/delete_post.html', context)