from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from mine import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # order details
    url(r'^order/detail/(?P<sn>\S+)/$', login_required(views.OrderDetailView.as_view()), name='order_detail'),
    # Add to cart
    url(r'^cart/add/(?P<prod_uid>\S+)/$', views.cart_add, name='cart_add'),
    # my shopping cart
    url(r'^cart/$', views.cart, name='cart'),
    # Submit Order
    url(r'^order/pay/$', views.order_pay, name='order_pay'),
    # My order list
    url(r'^order/list/$', login_required(views.OrderListView.as_view()), name='order_list'),
    # my collection
    url(r'^prod/collect/$', views.prod_collect, name='prod_collect'),
]