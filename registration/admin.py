


from django.contrib import admin
from .models import Custom_User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email')
    search_fields = ('first_name', 'last_name', 'username', 'email')

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'sender', 'receiver', 'message', 'timestamp')
#     search_fields = ('sender__username', 'receiver__username', 'message')

# Register the models and admin classes
admin.site.register(Custom_User, UserAdmin)
# admin.site.register(Message, MessageAdmin)
