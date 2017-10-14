from django.shortcuts import render
from rest_framework import viewsets, permissions
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from transactions.permissions import IsOwner

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)