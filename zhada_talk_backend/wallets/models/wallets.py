from django.db import models
from django.conf import settings
import uuid

User = settings.AUTH_USER_MODEL

class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - Balance: {self.balance}"

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('transfer', 'Transfer'),
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Wallet, related_name='sent_transactions', on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Wallet, related_name='received_transactions', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.transaction_type}: {self.amount}"
