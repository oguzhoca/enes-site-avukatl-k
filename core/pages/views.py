from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from . forms import ContactForm
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Mesajınızı Aldık'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class TeamView(TemplateView):
    template_name = 'team.html'