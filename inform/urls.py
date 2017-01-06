from django.conf.urls import url,include
from inform.views import *
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^input/', input_page),
    url(r'^page1/', part1_view),
    url(r'^api/?$', Clients.as_view()),
    url(r'^api/(?P<part1_id>[0-9]+)/?$', Clients.as_view()),

    ]