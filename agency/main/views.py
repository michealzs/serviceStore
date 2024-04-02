
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from .models import HomeModel, AboutModel

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

