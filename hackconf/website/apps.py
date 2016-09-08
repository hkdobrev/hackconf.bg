from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'hackconf.website'
    verbose_name = "Website"

    def ready(self):
        pass
