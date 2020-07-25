from django.contrib import admin
from .models import Language, Paradigm, Programmer

# admin.site.register(Language)
admin.site.register(Paradigm)
admin.site.register(Programmer)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    fields = ['name']  # show on edit/add form
    list_display = ['name', 'desc']  # list in admin side
    list_filter = ['name']
    search_fields = ['name']
