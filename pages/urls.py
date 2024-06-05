from django.urls import path

from pages.views import HomePageView, ContactTemplateView, ThankYouView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('contact/thank_you/', ThankYouView.as_view(), name='thank_you'),
]
