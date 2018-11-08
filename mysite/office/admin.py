from django.contrib import admin
from office.models import Engineer, Team, Product, Case, Advice

# Register your models here.
class EngineerAdmin(admin.ModelAdmin):
    list_display = ['engr_name', 'engr_team', 'title', 'vote', 'display_skills']
    list_filter = ['engr_team', 'title']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'queue', 'prod_team']
    list_filter = ['prod_team']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'ta_name', 'group']
    list_filter = ['team_name', 'group']

class AdviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'proposer']

# class CaseAdmin(admin.ModelAdmin):
#     list_display = ['id', 'number', 'title', 'c_description']

admin.site.register(Engineer, EngineerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Team, TeamAdmin)
#admin.site.register(Case, CaseAdmin)
admin.site.register(Advice, AdviceAdmin)
