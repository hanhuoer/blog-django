from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown

from comments.forms import CommentForm


def index (request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(
        request,
        'blog/index.html',
        context={
            'title': '首页_寒火儿的博客',
            'welcome': 'welcome to my blog, I\'m hanhuoer!',
            'post_list': post_list,
        }
    )

def detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, ['extra', 'codehilite', 'toc', ])

    form = CommentForm()
    comment_list = post.comment_set.all()

    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               }
    return render(request, 'blog/detail.html', context)



