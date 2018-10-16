"""
.. module:: project.settings.database
   synopsis: Database config
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'user',
        'PASSWORD': 'pwd',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
