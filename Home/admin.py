from django.contrib import admin

# Register your models here.
admin.site.site_header = "EHRS Header"
admin.site.site_title = "EHRS Title"
admin.site.index_title = "Welcome to Your EHRS Panel"
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

    def save_model(self, request, obj, form, change):
        print("Saving Contact:", obj.name)
        super().save_model(request, obj, form, change)

admin.site.register(Contact, ContactAdmin)


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
    