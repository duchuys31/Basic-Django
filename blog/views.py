from django.shortcuts import render, get_object_or_404
from .models import Post, comment
from django.views.generic import  ListView,DetailView
from .forms import comment_form
from django.http import HttpResponseRedirect

# Create your views here.

# def list(request):
#     Data = {'Posts': Post.objects.all().order_by("-date")}
#     return render(request, 'blog/blog.html',Data)

class Post_list_view(ListView):
    queryset = Post.objects.all().order_by("-date")
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1

# class Post_detail_view(DetailView):
#     model = Post
#     template_name = 'blog/post.html'

# def post(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'blog/post.html', {'post': post})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = comment_form()
    if request.method == 'POST':
        form = comment_form(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, 'blog/post.html', {'post':post, 'form':form})