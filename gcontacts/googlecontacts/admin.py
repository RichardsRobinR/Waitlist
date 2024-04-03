from django.contrib import admin
from .models import Contact, Adminusers

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone_number",
        "email",
    )


class AdminusersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "password",
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register(Adminusers, AdminusersAdmin)
