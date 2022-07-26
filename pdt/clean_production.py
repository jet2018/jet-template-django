from .settings import *
if not DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
    # AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_LOCATION = 'static_root'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    AWS_DEFAULT_ACL = None

    DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
    # Allow all host hosts/domain names for this site
    ALLOWED_HOSTS = ['*']

    # # # Parse database configuration from $DATABASE_URL

    DATABASES = {'default': dj_database_url.config()}

    # # # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    # https://docs.djangoproject.com/en/3.2/howto/static-files/
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

    MEDIA_URL = "/media/"

    MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
    try:
        DEBUG = True
        TEMPLATE_DEBUG = True

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    except Exception as e:
        pass
