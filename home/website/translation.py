from .models import HomePage
from modeltranslation.decorators import register
from wagtail_modeltranslation.translator import WagtailTranslationOptions

from wagtail_modeltranslation import patch_wagtailadmin

@register(HomePage)
class HomePageTranslationOptions(WagtailTranslationOptions):
    fields = ('slug', 'url_path', 'live', 'title', 'header_text', 'about_text', 'call_for_speakers_title')

    required_languages = ("bg", "en")
