from django.apps import AppConfig


class ManangeLinksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage_links'
    def ready(self):
        from . import signals
