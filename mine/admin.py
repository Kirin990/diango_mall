from django.contrib import admin

from mine.models import Order, Cart, Comments


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order background management """
    list_display = ('sn', 'user', 'to_user', 'to_area', 'to_phone')
    # Search by username and nickname
    search_fields = ('user__username', 'user__nickname', 'to_user')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """ Shopping cart management """
    list_display = ('name', 'user', 'price', 'img')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """ Product Reviews """
    list_display = ('user', 'product', 'score', 'desc')



