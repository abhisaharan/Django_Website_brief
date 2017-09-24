from django.conf.urls import url
from . import views

app_name = 'music'  #we mentioned app_name here. So that in when html we will use 'music:detail'. It will not be confusing cause we will know 'detail' view belong to which app and also we can use 'detail' word for another view
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),    #as_view converts classes in views.py to view
    url(r'^register/$', views.UserFromView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'^album/add/', views.AlbumCreate.as_view(), name='album-add'), # in tutorial it was like "r'^album/add/$'" but for me it worked without $ sign
    url(r'^album/(?P<pk>[0-9]+)/', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]