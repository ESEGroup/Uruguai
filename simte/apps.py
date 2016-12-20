from django.apps import AppConfig


class SimteConfig(AppConfig):
    name = 'simte'

    def ready(self):
        import simte.signals
