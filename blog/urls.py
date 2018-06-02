''' To create individual urls for blog entries '''

from django.conf.urls import url
from . import views

# individual regex pattern for blog-enty-http
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]