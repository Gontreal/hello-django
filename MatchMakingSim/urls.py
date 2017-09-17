from django.conf.urls import url
from . import views

app_name='matches'
urlpatterns=[
    url(r'^$', views.intro, name='intro'),
    url(r'^matching/$',views.match_engine, name='matching')
]