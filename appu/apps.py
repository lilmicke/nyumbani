from django.apps import AppConfig

class AppuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Optional: Set the default auto field type
    name = 'appu'  # The name of your app
    label = 'appu'  # The label for your app, typically the app name in lowercase
