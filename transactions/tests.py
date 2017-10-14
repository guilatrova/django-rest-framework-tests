from django.test import TestCase
from django.urls import reverse, resolve

from transactions.views import TransactionViewSet

class TransactionsUrlsTestCase(TestCase):

    def test_resolves_list_url(self):
        resolver = self.resolve_by_name('transactions')
        
        self.assertEqual(resolver.func.cls, TransactionViewSet)

    def test_resolves_retrieve_url(self):
        resolver = self.resolve_by_name('transaction', pk=1)
        
        self.assertEqual(resolver.func.cls, TransactionViewSet)

    def test_resolves_url_to_list_action(self):
        resolver = self.resolve_by_name('transactions')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = self.resolve_by_name('transaction', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])        

    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)