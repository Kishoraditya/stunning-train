from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    def ready(self):
        # Import the modeladmin to ensure it registers with Wagtail
        import api.modeladmin
