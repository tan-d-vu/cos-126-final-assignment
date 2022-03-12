from django.apps import AppConfig


class ManangeUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manage_users'
    def ready(self):
        from . import signals