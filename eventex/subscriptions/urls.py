from django.urls import path
from eventex.subscriptions.views import new, detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<str:hash_pk>/', detail, name='detail'),
]
