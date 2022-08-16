# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-nh9mfvjq*s5%o%_2)9ef68(zfscp8zh6i4@(dfd#%*@af76d%n"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'music_database',
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "hatemenow",
        "PORT": "3306",
        "OPTIONS": {
       "autocommit": True
        }

        }
}