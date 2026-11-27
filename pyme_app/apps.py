from django.apps import AppConfig


class PymeAppConfig(AppConfig):
    name = 'pyme_app'

    def ready(self):
        import pyme_app.signals
