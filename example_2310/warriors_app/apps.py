from django.apps import AppConfig
from django.core.signals import request_finished


class WarriorsAppConfig(AppConfig):
    name = 'warriors_app'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
        # Explicitly connect a signal handler.
        #request_finished.connect(signals.my_handler, sender=self)
