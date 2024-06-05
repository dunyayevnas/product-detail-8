from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.core.mail import send_mail
from pages.models import *


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    model = InfoModel
    context_object_name = 'Ninfo'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['Ninfo'] = InfoModel.objects.all()

        return content


class ContactTemplateView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:thank_you')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(
            'Sizga taklifim bor !',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            'sotvoldiyevazamat193@gmail.com.com',
            ['sotvoldiyevazamat193@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'
