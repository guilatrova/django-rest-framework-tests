from django.conf.urls import url
from transactions import views

list_actions = {
    'get': 'list',
    'post': 'create'
}

single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    url(r'^$', views.TransactionViewSet.as_view(list_actions), name="transactions"),
    url(r'^(?P<pk>\d+)$', views.TransactionViewSet.as_view(single_actions), name='transaction'),
]