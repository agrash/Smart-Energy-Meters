from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^index/$', views.index, name = 'index'),
    url(r'^Bharti/$', views.Bharti, name = 'Bharti'),
    url(r'^SIT/$', views.SIT, name = 'SIT'),
    url(r'^Block4/$', views.Block4, name = 'Block4'),
    url(r'^Block6/$', views.Block6, name = 'Block6'),
    url(r'^Girnar/$', views.Girnar, name = 'Girnar'),
    url(r'^Udaigiri/$', views.Udaigiri, name = 'Udaigiri'),
    url(r'^Overview/$', views.Overview, name = 'Overview'),
]
