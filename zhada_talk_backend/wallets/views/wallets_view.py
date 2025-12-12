from rest_framework import viewsets, status
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models.wallets import Wallet, Transaction
from ..serializers.wallets_serializer import WalletSerializer, TransactionSerializer, WalletTransferSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users see only their own wallet
        return Wallet.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def transfer(self, request, pk=None):
        wallet = self.get_object()
        serializer = WalletTransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data['amount']
        receiver_id = serializer.validated_data['receiver_id']

        if wallet.balance < amount:
            return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

        receiver_wallet = get_object_or_404(Wallet, id=receiver_id)

        wallet.balance -= amount
        receiver_wallet.balance += amount
        wallet.save()
        receiver_wallet.save()

        Transaction.objects.create(
            sender=wallet,
            receiver=receiver_wallet,
            amount=amount,
            transaction_type='transfer',
            description=f'Transfer to {receiver_wallet.user.email}'
        )

        return Response({"status": "Transfer successful"})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_wallet = getattr(self.request.user, 'wallet', None)
        if user_wallet:
            return Transaction.objects.filter(Q(sender=user_wallet) | Q(receiver=user_wallet))
        return Transaction.objects.none()

