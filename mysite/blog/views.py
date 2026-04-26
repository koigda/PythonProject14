from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm, SubscriptionForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    comment_form = CommentForm()
    subscription_form = SubscriptionForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

        elif 'subscribe_submit' in request.POST:
            subscription_form = SubscriptionForm(request.POST)
            if subscription_form.is_valid():
                subscription_form.save()

        return redirect('post_detail', pk=post.pk)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'subscription_form': subscription_form
    })