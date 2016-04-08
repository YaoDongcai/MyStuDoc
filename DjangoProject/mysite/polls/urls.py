__author__ = 'yaodongcai'
from django.conf.urls import include, url
from polls import views
from django.contrib import admin

urlpatterns = [
    url(r'index', views.index,name="index"),
    url(r'about', views.about,name="about"),
    # url(r'(P<question_id>[0-9]+)/$',views.detail,name="detail"),
]
