from django.conf.urls import url
from . import views

app_name='games'
urlpatterns=[
    url(r'^$',views.index, name='welcome'),
    url(r'^gameon/$',views.game_engine, name='engine')
]