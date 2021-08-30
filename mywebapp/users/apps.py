from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # from django documentation,
    # see django -> topics -> signals -> "Where should this code live?"
    def ready(self):
        import users.signals
