__author__ = 'yaodongcai'
from django.conf.urls import include, url
from polls import views
from django.contrib import admin

urlpatterns = [
    url(r'index', views.index,name="index"),#这个是首页page
    url(r'about', views.about,name="about"),#这个是关于我们page
    url(r'contact',views.contact,name="contact"),#这个是联系我们page，
    url(r'order', views.order,name="order"),#这个是我们的订单
    # url(r'(P<question_id>[0-9]+)/$',views.detail,name="detail"),
]
