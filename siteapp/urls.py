from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$', views.load_page, name='about'),
    url(r'^music/$', views.music, name='music'),
    url(r'^music/(?P<album_title>.+)/$', views.new_album, name='album'),
    url(r'^view/$', views.media, name='media'),
    url(r'^view/video/(?P<idnum>.+)/$', views.video, name='video'),
    url(r'^view/photo/(?P<idnum>.+)/$', views.photo, name='photo'),
    url(r'^social/$', views.load_page, name='social'),
    url(r'^contact/$', views.load_page, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks')
]
