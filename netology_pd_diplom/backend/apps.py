from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = 'backend'
    default_auto_field = 'django.db.models.BigAutoField'


  #  def ready(self):
       # """
        #импортируем сигналы
        #"""
