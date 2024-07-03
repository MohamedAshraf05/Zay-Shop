from django.apps import AppConfig


class ZayappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zayapp'

    def ready(self):
        import zayapp.signals