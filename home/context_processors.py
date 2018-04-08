from django.conf import settings


def app_settings(request):
    return {
        'GA_TRACKING_ID': settings.GA_TRACKING_ID
    }
