from django.apps import AppConfig


class MentorshipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mentorship'

    # connect signals when app is ready 
    def ready(self):
        import mentorship.signals
