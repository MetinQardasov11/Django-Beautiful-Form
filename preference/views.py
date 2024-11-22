from django.shortcuts import render
from .models import Preference
from .forms import PreferenceForm
from django.views.generic import FormView
from django.contrib import messages

class PreferenceFormView(FormView):
    form_class = PreferenceForm
    template_name = 'preference/main.html'
    
    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Send Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.add_error(None, 'Ups ... Something went wrong')
        return super().form_invalid(form)