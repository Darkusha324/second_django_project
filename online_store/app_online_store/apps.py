from django.apps import AppConfig

class AppOnlineStoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_online_store'

    def ready(self):
        import app_online_store.signals
