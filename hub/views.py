from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Post

@login_required
def home(request):
    # Making it so ony user1 and user2 can post for now.
    can_post = request.user.username in ['user1', 'user2']

    if request.method == 'POST' and can_post:
        text = request.POST.get('text')
        if text:
            Post.objects.create(user=request.user, text=text)
        return redirect('home')

    # Everyone sees all posts, for now will come back to fix this. Potentially adding categories so users can only view Sports, Talks, Science ect.
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'hub/home.html', {'posts': posts, 'can_post': can_post})

# Admin can be the only one to delete for now, might give users the power to delete their own post.
@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home')
