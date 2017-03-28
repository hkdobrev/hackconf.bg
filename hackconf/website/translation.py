from .models import HomePage
from modeltranslation.decorators import register
from wagtail_modeltranslation.translator import WagtailTranslationOptions

@register(HomePage)
class HomePageTranslationOptions(WagtailTranslationOptions):
    fields = ('live_stream', 'header_dates', 'header_text', 'about_text', 'title')
