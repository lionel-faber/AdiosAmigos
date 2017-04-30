from django.contrib import admin

# Register your models here.
from .models import  Bubye, List
from django.contrib.auth.models import User

class BubyeAdmin(admin.ModelAdmin):
    '''
        Admin View for Bubye
    '''
    model = Bubye
    list_display = ('get_name','message')
    list_filter = ('alumini',)
    def get_name(self, obj):
	    return obj.alumini.name
    get_name.admin_order_field = 'alumni'
    get_name.short_description = 'alumni'


admin.site.register(List)
admin.site.register(Bubye, BubyeAdmin)
# admin.site.register(Bubye)
