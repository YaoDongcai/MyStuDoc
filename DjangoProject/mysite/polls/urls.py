__author__ = 'yaodongcai'
from django.conf.urls import include, url
from polls import views
from django.contrib import admin

urlpatterns = [
    url(r'index', views.index,name="index"),#�������ҳpage
    url(r'about', views.about,name="about"),#����ǹ�������page
    url(r'contact',views.contact,name="contact"),#�������ϵ����page��
    url(r'order', views.order,name="order"),#��������ǵĶ���
    # url(r'(P<question_id>[0-9]+)/$',views.detail,name="detail"),
]
