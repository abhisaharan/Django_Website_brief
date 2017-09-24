from django.conf.urls import url
from . import views

app_name = 'music'  #we mentioned app_name here. So that in when html we will use 'music:detail'. It will not be confusing cause we will know 'detail' view belong to which app and also we can use 'detail' word for another view
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),

]