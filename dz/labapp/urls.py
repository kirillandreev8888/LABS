from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^success_authorization_dumb$', views.success_authorization_dumb, name='success_authorization_dumb'),
    url(r'^success_authorization$', views.success_authorization, name='success_authorization'),
    url(r'^authorization/$', views.authorization, name='authorization'),
    url(r'^registration_dumb/$', views.registration_dumb, name='registration_dumb'),
    url(r'^registration_user/$',views.registration_user, name='registration_user'),
    url(r'^add_film/$', views.add_film, name='add_film'),
    url(r'^users/$',views.UserList.as_view(),name='user_list'),
    url(r'^films/$',views.FilmList.as_view(),name='film_list'),
    url(r'^reviews/$',views.ReviewList.as_view(),name='review_list'),
    url(r'^$', views.index, name='index'),
]