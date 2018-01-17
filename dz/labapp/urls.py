from django.conf.urls import url

from . import views

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import *
from django.views.generic import DetailView

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
    url(r'^film/(?P<pk>\d+)$', views.film_view.as_view(), name='film_view'),
    url(r'^add_review/(?P<film_id>[A-Za-z0-9- ]+)$', views.add_review, name='add_review')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)