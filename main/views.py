
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView, FormView
from .models import HomeModel, AboutModel
from .form import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

class HomeView(ListView):
    model = HomeModel
    template_name = 'indexx.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(50*'8', '\n', self.request.META.get('HTTP_X_REAL_IP'), "Just Visited US", '\n', 50*'8')
        if self.request.user.is_authenticated:
            print('pure user ==>', self.request.user)
            print('pure username ==>', self.request.user.username)
            #print('pure email ==>', self.request.user.email)
            #print(50*'#', 'Session ===>', self.request.session)
            #print('pure META ==>', self.request.META)
            #print('pure Visitor ID ==>', self.request.session['visitor_id'])
        else:
            print("<== User is not Authenticated ==>")
        return context

    """
    def dispatch(self, request, *args, **kwargs):
        sessione(self.request)
        return super().dispatch(request, *args, **kwargs)
    """

class AboutView(TemplateView):
    template_name = 'about-us.html'

class FaqView(TemplateView):
    template_name = 'faq.html'


class GrapDesignView(TemplateView):
    template_name = 'graphic-design.html'


class WebDesignView(TemplateView):
    template_name = 'web-design.html'


class MobDesignView(TemplateView):
    template_name = 'mobile-design.html'


class MarkettingView(TemplateView):
    template_name = 'digital-marketting.html'


class AppSupportView(TemplateView):
    template_name = 'app-support.html'

class WebRadioView(TemplateView):
    template_name = 'web-radio.html'


class JobOpeningView(TemplateView):
    template_name = 'openings.html'

class SuccessView(TemplateView):
    template_name = 'success.html'

class ContactFormView(CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Save the form data to the database
        name = form.cleaned_data['conName']
        email = form.cleaned_data['conEmail']
        message = form.cleaned_data['conMessage']
        print(f"Name: {name}, Email: {email}, Message: {message}")

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send an email with the form data
        send_mail(
            'New Contact Form Submission',
            f'From: {name}, Email: {email}, Message: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        return super().form_valid(form)