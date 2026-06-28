from modeltranslation.translator import register, TranslationOptions
from .models import Competitions

@register(Competitions)
class CompetitionsTranslation(TranslationOptions):
    fields = ('name', 'description')