from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from hashids import Hashids


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    subscription = form.save()
    # Send subscription email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})
    return HttpResponseRedirect(r('subscriptions:detail', _hash_pk(subscription.pk)))


def detail(request, hash_pk):
    try:
        pk = _unhash_pk(hash_pk)
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])


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
