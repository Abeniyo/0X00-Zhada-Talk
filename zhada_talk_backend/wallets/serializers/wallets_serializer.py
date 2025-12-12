from rest_framework import serializers
from ..models.wallets import Wallet, Transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class WalletSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Wallet
        fields = ['id', 'user', 'user_email', 'balance', 'created_at']
        read_only_fields = ['balance', 'created_at']

class TransactionSerializer(serializers.ModelSerializer):
    sender_email = serializers.ReadOnlyField(source='sender.user.email')
    receiver_email = serializers.ReadOnlyField(source='receiver.user.email')

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'sender_email', 'receiver', 'receiver_email', 'amount', 'transaction_type', 'timestamp', 'description']
        read_only_fields = ['timestamp']

class WalletTransferSerializer(serializers.Serializer):
    receiver_id = serializers.UUIDField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value
