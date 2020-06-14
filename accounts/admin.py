from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from accounts.models import User, UserProfile, UserAddress


@admin.register(User)
class UserAdmin(UserAdmin):
    """ Basic user information """
    # fields = ('integral', 'level', 'nickname')
    list_display = ('format_username', 'nickname', 'integral', 'is_active')
    # Support searching by user name and nickname
    search_fields = ('username', 'nickname')
    # Add custom methods
    actions = ['disable_user', 'enable_user']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name',
                                        'email', 'integral', 'nickname')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def format_username(self, obj):
        """ User name desensitization """
        return obj.username[0:3] + '***'

    # Modify column name display
    format_username.short_description = 'username'

    def disable_user(self, request, queryset):
        """ Disable selected users in batch """
        queryset.update(is_active=False)

    disable_user.short_description = 'Disable users in batches'

    def enable_user(self, request, queryset):
        """ Enable selected users in batch """
        queryset.update(is_active=True)

    enable_user.short_description = 'Enable users in batches'


# admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """ User details """
    list_display = ('user', 'phone_no', 'sex')


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    """ User address management """
    list_display = ('user', 'province', 'city',
                    'username', 'address', 'phone',
                    'is_valid', 'is_default')
    search_fields = ('user__username', 'user__nickname',
                     'phone', 'username')
