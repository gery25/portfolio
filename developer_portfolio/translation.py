from modeltranslation.translator import register, TranslationOptions
from .models import Project

@register(Project)
class ProjectTranslation(TranslationOptions):
    fields = ('name', 'description')
