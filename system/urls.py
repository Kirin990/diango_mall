from django.conf.urls import url

from system import views

urlpatterns = [
    # news list
    url(r'^news/$', views.news_list, name='news_list'),
    # News details
    url(r'^new/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),

    # verify code
    url(r'^verify/code/$', views.verify_code, name='verify_code'),
]