

from django.urls import path, include
from .views import (
    HomeView,
    AboutView,
    FaqView,
    GrapDesignView,
    WebDesignView,
    MobDesignView,
    MarkettingView,
    AppSupportView,
    WebRadioView,
    JobOpeningView,
)

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('faq', FaqView.as_view(), name='faq'),
    path('graphic-design', GrapDesignView.as_view(), name='graphic-design'),
    path('web-design', WebDesignView.as_view(), name='web-design'),
    path('mobile-design', MobDesignView.as_view(), name='mobile-design'),
    path('digital-marketting', MarkettingView.as_view(), name='digital-marketting'),
    path('app-support', AppSupportView.as_view(), name='app-support'),
    path('web-radio', WebRadioView.as_view(), name='web-radio'),
    path('openings', JobOpeningView.as_view(), name='openings'),

]