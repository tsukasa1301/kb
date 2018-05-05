import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django import forms

from myapp.models import Episode
from myapp.forms import EpisodeForm, ContactForm

from django.views.generic.edit import FormView
from .forms import ContactForm
from django.views import View
from django.core.mail import EmailMessage, send_mail
from myproject import settings
from django.contrib.auth.models import User




def index(request):
    return render(request, 'myapp/index.html', {})


def about(request):
    return render(request, 'myapp/about.html', {})


def contact(request):
    return render(request, 'myapp/contact.html', {})


def Contribution(request):
    return render(request, 'myapp/Contribution.html', {})


def episode(request):
    e = Episode.objects.all()
    return render(request, 'myapp/episode.html', {'new_episode': e})


def policy(request):
    return render(request, 'myapp/policy.html', {})


def kiyaku(request):
    return render(request, 'myapp/kiyaku.html', {})



def toukou(request):
    if request.method == 'POST':
        form = EpisodeForm(request.POST)
        if form.is_valid():
            episode = form.save(commit=False)
            episode.save()
            #return  HttpResponse("ご投稿いただきありがとうございました！是非他の方の体験談もご覧ください！")
            return redirect('myapp:episode')
    else:
        return redirect('myapp:Contribution')
    #new_episode = Episode.objects.all().order_by('id')
    #contexts = {
    #    'form':form,
    #    'new_episode':new_episode,
    #    }
    
    #return render(request, 'myapp/episode.html', contexts)


class ContactView(FormView):
    form_class = ContactForm
    success_url = '/index/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
    

#def ContactView(request):
 #   if request.method == 'POST':
 #       form = ContactForm(request.POST)
 #       if form.is_valid():
 #           form.send_email()
 #           return super(ContactView, self).form_valid(form)

#    else:
#        return redirect('myapp:contact')
