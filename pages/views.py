# *-* coding: utf-8 *-*
from django.shortcuts import render, render_to_response
from pages.forms import ContactForm, ItemForm, StatusForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from pages.models import Contact
from django.core.mail import send_mail

def home(request):
    context = RequestContext(request)
    return render(request, 'index.html', context)

def status(request):
    context = RequestContext(request)
    context = RequestContext(request)
    context['form'] = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            get_item = Contact.objects.filter(email=email)
            return HttpResponseRedirect('/status/')
    return render(request, 'status.html', context)

def get_entry(request, email):
    get_item = Contact.objects.filter(email=email)

def upload_stat(request):
    if request.method == "GET":
        dump = open('gallery/upload_state.json', 'r')
        return HttpResponse(dump, content_type='application/json')


def contact(request):
    context = RequestContext(request)
    context['form'] = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            place = form.cleaned_data['place']
            length = form.cleaned_data['length'] # Need To be Fixed!
            #new_contact.save()
            mail = 'Уважаемый клиент, статус вашего заказа вы можете здесь http://127.0.0.1:8000/status'
            send_mail('Заказ сьемки у Weeding Photo Kiev',
                      mail,
                      'hector007@pochta.ru',
                      [email], fail_silently=False)
            return HttpResponseRedirect('/status/')

    return render(request, 'contact.html', context)