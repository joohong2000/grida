from django.urls import path

from subscribeapp.views import SubscriptionView

from subscribeapp.views import SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
]
