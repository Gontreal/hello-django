from django.conf.urls import url
from . import views
# from django.views.generic import DetailView, ListView
# from blog.models import Post

app_name = "blogs"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="List"),
    url(r'^(?P<pk>\d+)$', views.DetailView.as_view(), name="Detail")
]
