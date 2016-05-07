from django.contrib import admin
from .models import Authors


class AuthorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name','surname',)}

admin.site.register(Authors,AuthorsAdmin)
#admin.site.register(Authors)
