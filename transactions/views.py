from django.shortcuts import render
from rest_framework import viewsets, permissions
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from transactions.permissions import IsOwner

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer