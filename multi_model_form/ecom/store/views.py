from django.shortcuts import render

# views.py
from django.views.generic.base import TemplateView
from .models import Person, Bio, Email
from .forms import PersonForm, BioForm, EmailForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class PersonDetailUpdateView(TemplateView):
    template_name = 'planner/person_detail_update_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = get_object_or_404(Person, pk=self.kwargs['pk'])
        context['person'] = person
        context['person_form'] = PersonForm(instance=person)
        context['bio_form'] = BioForm(instance=person.bio)
        context['email_form'] = EmailForm(instance=person.email)
        return context

