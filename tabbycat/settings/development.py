import os

from core import *


# ==============================================================================
# Templates
# ==============================================================================

# Don't used the cached loader otherwise updating templates is a pain
# TEMPLATES[0]['OPTIONS']['loaders'] = [
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# ]

# ==============================================================================
# Webpack
# ==============================================================================

# Enables hot reloading but relies on the vue-cli (webpack) server being run
USE_WEBPACK_SERVER = True

# ==============================================================================
# Debug Toolbar
# ==============================================================================

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/js/vendor/jquery.js', # Enables offline work
    'SHOW_COLLAPSED': True
}

ENABLE_DEBUG_TOOLBAR = True
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
INSTALLED_APPS += ('debug_toolbar',)
# Override check for internal IPs (and DEBUG=1) on Heroku
DEBUG_TOOLBAR_CONFIG['SHOW_TOOLBAR_CALLBACK'] = 'settings.show_toolbar'

# ==============================================================================
# Redis
# ==============================================================================

USE_REDIS_LOCALLY = False

# Option to run channels/cache on Redis locally (requires redis install)
if USE_REDIS_LOCALLY:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("localhost", 6379)],
            },
        },
    }
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "IGNORE_EXCEPTIONS": True, # Don't crash on say ConnectionError due to limits
            }
        }
    }

# ==============================================================================
# Debug Toolbar (development aid; helps diagnose queries and performance)
# ==============================================================================

ENABLE_DEBUG_TOOLBAR = True # True requires requirements_development install

if ENABLE_DEBUG_TOOLBAR:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
    INSTALLED_APPS += ('debug_toolbar',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'ddt_request_history.panels.request_history.RequestHistoryPanel',
    )
