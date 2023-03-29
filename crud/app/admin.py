from django.contrib import admin
from .models  import   user
# Register your models here.


admin.site.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('id','name','password' , 'email ')