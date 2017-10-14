from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from transactions.views import TransactionViewSet
from transactions.serializers import TransactionSerializer

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

class TransactionsSerializersTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester')
        self.serializer_data = {
            'description': 'description', 
            'value': 10,
            'user': self.user.id
        }

    def test_serializer_should_not_allows_value_0(self):
        data = self.serializer_data
        data['value'] = 0

        serializer = TransactionSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('value', serializer.errors)

    def test_serializer_validates_correctly_data(self):
        serializer = TransactionSerializer(data=self.serializer_data)

        self.assertTrue(serializer.is_valid())
