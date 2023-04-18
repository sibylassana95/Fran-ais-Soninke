from django.contrib import admin

from .models import Traduction


class TraductionAdmin(admin.ModelAdmin):
    list_display = ('francais', 'soninke')
    list_filter = ('francais',)
    search_fields = ('francais', 'soninke')
    list_per_page = 50


admin.site.register(Traduction, TraductionAdmin)
