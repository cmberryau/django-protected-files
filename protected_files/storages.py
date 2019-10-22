from django.conf import settings
from django.utils.functional import cached_property
from django.core.files.storage import FileSystemStorage


class ProtectedStorage(FileSystemStorage):
    @property
    def _root(self):
        raise NotImplementedError

    @property
    def _url(self):
        raise NotImplementedError

    @cached_property
    def base_location(self):
        return self._value_or_setting(self._location, self._root)

    @cached_property
    def base_url(self):
        if self._base_url is not None and not self._base_url.endswith('/'):
            self._base_url += '/'
        return self._value_or_setting(self._base_url, self._url)


class ProtectedMediaStorage(ProtectedStorage):
    @property
    def _url(self):
        return settings.PROTECTED_MEDIA_ROOT

    @property
    def _root(self):
        return settings.PROTECTED_MEDIA_URL


class ProtectedStaticStorage(ProtectedStorage):
    @property
    def _url(self):
        return settings.PROTECTED_STATIC_ROOT

    @property
    def _root(self):
        return settings.PROTECTED_STATIC_URL
