from .settings_common import *

DEBUG = True

# settings of logging
LOGGING = {
    "version": 1,
    "disable_exisiting_logger": False,
    
    # Logger 
    "loggers": {
        # Logger for django
        "django" : {
            "handlers":["console"],
            "level": "INFO",
        },
        # Logger for coupon application
        "coupon":{
            "handlers":["console"],
            "level": "DEBUG",
        }
    },

    # Settings of handlers
    "handlers" : {
        "console": {
            "level" : "DEBUG",
            "class" : "logging.StreamHandler",
            "formatter": "dev"
        },
    },

    # Settings of formatter
    "formatters": {
        "dev" : {
            "format" : "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d",
                "%(message)s"
            ])
        },
    }
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
    os.path.join(BASE_DIR,"media"),
)