from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Competitions

# Register your models here.
@admin.register(Competitions)
class CompetitionsAdmin(TranslationAdmin):
    pass
