import sys
import django

from django.conf import settings
from django.test.utils import get_runner

settings.configure(
    HOST_NAME='localhost',
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    ROOT_URLCONF='urls',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.messages',
    ],
    MIDDLEWARE=[
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    TEMPLATES=[
        {
            'APP_DIRS': True,
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                'templates',
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    AUTH_PASSWORD_VALIDATORS=[
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ],
    TEST_RUNNER='xmlrunner.extra.djangotestrunner.XMLTestRunner',
    TEST_OUTPUT_FILE_NAME='test-results.xml',
)

django.setup()

# get a test runner
test_runner = get_runner(settings)(verbosity=1)

failures = test_runner.run_tests(test_labels=['protected_files'])

if failures:
    sys.exit(failures)
