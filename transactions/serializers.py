from rest_framework import serializers
from transactions.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'description', 'value', 'user')

    def validate_value(self, value):
        if value == 0:
            raise serializers.ValidationError('Value cannot be 0')

        return value