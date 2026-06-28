from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Project, Skill

# Register your models here.

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    pass
admin.site.register(Skill)
