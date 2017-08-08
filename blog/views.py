from django.shortcuts import render


from django.views import generic
from .models import Post
# Create your views here.
class IndexView(generic.ListView):
    template_name = "blog/blog.html"
    context_object_name = 'latest_posts_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.all().order_by("-date")[:25]
        
class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
