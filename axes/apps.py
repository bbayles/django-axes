from django import apps
from django.utils.decorators import method_decorator


class AppConfig(apps.AppConfig):
    name = 'axes'

    def ready(self):
        from django.contrib.auth.views import LoginView
        from axes.decorators import watch_login

        LoginView.dispatch = method_decorator(watch_login)(LoginView.dispatch)
