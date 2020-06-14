from django.contrib import messages


def set_invalid(modeladmin, request, queryset):
    """ Batch disabled is_valid=False """
    queryset.update(is_valid=False)
    messages.success(request, 'Successful operation')


set_invalid.short_description = 'Disable selected objects'


def set_valid(modeladmin, request, queryset):
    """ Batch activation is_valid=True """
    queryset.update(is_valid=True)
    messages.success(request, 'Successful operation')


set_valid.short_description = 'Enable selected objects'
