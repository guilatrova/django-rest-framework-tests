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

    def test_list_url_only_allows_get_and_post(self):
        resolver = self.resolve_by_name('transactions')

        self.assert_has_actions(['get', 'post'], resolver.func.actions)

    def test_single_url_allows_all_methods_except_post(self):
        """All methods are: GET, PUT, PATCH and DELETE"""
        resolver = self.resolve_by_name('transaction', pk=1)

        self.assert_has_actions(['get', 'put', 'patch', 'delete'], resolver.func.actions)
        
    def assert_has_actions(self, allowed, actions):
        self.assertEqual(len(allowed), len(actions))

        for allows in allowed:
            self.assertIn(allows, actions)

    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)