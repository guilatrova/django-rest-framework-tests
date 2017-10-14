from django.conf.urls import url
from transactions import views

urlpatterns = [
    url(r'^$', views.TransactionViewSet.as_view({ 'get': 'list' }), name="transactions"),
    url(r'^(?P<pk>\d+)$', views.TransactionViewSet.as_view({ 'get': 'retrieve' }), name='transaction'),
]