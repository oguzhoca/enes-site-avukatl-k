from django.urls import path
from .views import AboutView, IndexView, ContactView, ServiceView, TeamView
from . import views



urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('hakkimizda/', AboutView.as_view(), name="about"),
    path('iletisim/', ContactView.as_view(), name="contact"),
    path('hizmetlerimiz/', ServiceView.as_view(), name="service"),
    path('ekibimiz/', TeamView.as_view(), name="team"),


    #path('contact/', ContactView.as_view(), name="contact"),
]