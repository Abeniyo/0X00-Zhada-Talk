from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.wallets_view import WalletViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = router.urls
