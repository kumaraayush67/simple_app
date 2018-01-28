from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^add/', views.CreateUser.as_view(), name='add'),

    url(r'^(?P<pk>[0-9]+)/delete/', views.DeleteUser.as_view(), name='delete'),

    url(r'^(?P<pk>[0-9]+)/update/', views.UpdateUser.as_view(), name='update'),
]
