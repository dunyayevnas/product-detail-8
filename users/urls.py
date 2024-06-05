from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('wishlist', WishlistView.as_view(), name='wishlist'),
    path('card/', CartView.as_view(), name='card'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('account/', AccountView.as_view(), name='account'),
    path('verify/email',verify_email, name='verify-email'),
    path('logout/', logout_view ,name='logout'),
]