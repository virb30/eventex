from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from hashids import Hashids

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')


def detail(request, hash_pk):
    try:
        pk = _unhash_pk(hash_pk)
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _hash():
    hashids = Hashids(salt=settings.HASH_SALT)
    return hashids


def _hash_pk(pk):
    hasher = _hash()
    return hasher.encode(pk)


def _unhash_pk(hashed):
    hasher = _hash()
    decoded = hasher.decode(hashed)
    return decoded[0] if decoded else 0
