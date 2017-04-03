from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'home.website'
    verbose_name = "Website"

    def ready(self):
        pass
