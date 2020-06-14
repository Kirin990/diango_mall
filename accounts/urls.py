from django.conf.urls import url

from accounts import views

urlpatterns = [
    # User login
    url(r'^user/login/$', views.user_login, name='user_login'),
    # User exit
    url(r'^user/logout/$', views.user_logout, name='user_logout'),
    # User registration
    url(r'^user/register/$', views.user_register, name='user_register'),

    # Address list
    url(r'^user/address/list/$', views.address_list, name='address_list'),
    # Address modification and editing
    # user/address/edit/add/   user/address/edit/12/
    url(r'^user/address/edit/(?P<pk>\S+)/$', views.address_edit, name='address_edit'),
    url(r'^user/address/delete/(?P<pk>\d+)/$', views.address_delete, name='address_delete'),
]