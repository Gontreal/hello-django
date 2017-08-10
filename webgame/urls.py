from django.conf.urls import url
from . import views
from .game import map
app_name='games'
urlpatterns=[
    url(r'^$',views.index, name='welcome'),
    url(r'^gameon/$',views.game_engine, name='engine')
]