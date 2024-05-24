from django.views.generic.base import TemplateView
from .models import Person, Bio, Email
from .forms import PersonForm, BioForm, EmailForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

class PersonDetailUpdateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person = get_object_or_404(Person, pk=self.kwargs['pk'])
        context['person'] = person
        context['person_form'] = PersonForm(instance=person)
        context['bio_form'] = BioForm(instance=person.bio)
        context['email_form'] = EmailForm(instance=person.email)
        return context
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        person = get_object_or_404(Person, pk=pk)
        person_form = PersonForm(instance=person, data=request.POST)
        bio = get_object_or_404(Bio, person__pk=pk)
        bio_form = BioForm(instance=bio, data=request.POST)
        email = get_object_or_404(Email, person__pk=pk)
        email_form = EmailForm(instance=email, data=request.POST)
        
        if 'save_person' in request.POST:
            if person_form.is_bound and person_form.is_valid():
                person_form.save()
                messages.add_message(request, messages.SUCCESS, f"{person.pk} {person.name} {person.age} {person.status}")
            else:
                messages.error(request, person_form.errors)
        
        elif 'save_bio' in request.POST:
            if bio_form.is_bound and bio_form.is_valid():
                bio_form.save()
                messages.add_message(request, messages.SUCCESS, f'{bio.person.pk} {bio.bio} {bio.image} saved')
            else:
                messages.error(request, bio_form.errors)
        
        elif 'save_email' in request.POST:
            if email_form.is_bound and email_form.is_valid():
                email_form.save()
                messages.add_message(request, messages.SUCCESS, f'{email.person.pk} {email.address}')
            else:
                messages.error(request, email_form.errors)
        
        return HttpResponseRedirect(reverse('planner:person_detail_update_form', kwargs={'pk': self.kwargs['pk']}))

