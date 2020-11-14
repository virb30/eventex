from django.conf import settings
from hashid_field import Hashid


def make_hash(pk):
    return Hashid(pk, min_length=settings.HASHID_MIN_LENGTH, salt=settings.HASHID_FIELD_SALT)