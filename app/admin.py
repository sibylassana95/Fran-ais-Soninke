from django.contrib import admin

from .models import Traduction,Contribution


class TraductionAdmin(admin.ModelAdmin):
    list_display = ('francais', 'soninke')
    list_filter = ('francais',)
    search_fields = ('francais', 'soninke')
    list_per_page = 100

class ContributionAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'francais', 'soninke')



admin.site.register(Contribution, ContributionAdmin)
admin.site.register(Traduction, TraductionAdmin)
