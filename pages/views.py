# *-* coding: utf-8 *-*
from django.shortcuts import render, render_to_response
from pages.forms import ContactForm, ItemForm, StatusForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from pages.models import Contact
from django.core.mail import send_mail
import json
from django.views.decorators.csrf import csrf_exempt
import time

def home(request):
    context = RequestContext(request)
    return render(request, 'index.html', context)

def status(request):
    context = RequestContext(request)
    context['form'] = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            get_item = Contact.objects.filter(email=email)
            return HttpResponseRedirect('/status/')
    return render(request, 'status.html', context)

@csrf_exempt
def status_json(request):
    if request.method == 'GET':
        data = request.GET.get('email')
        print data
        get_item = Contact.objects.filter(email=data)
        if get_item:
            i=0
            json_data = {}
            for item in get_item:
                i=i+1
                item_time =  item.pub_date.strftime('%d.%m.%Y %H:%M')
                json_data[i]= {}
                json_data[i]['email'] = item.email
                json_data[i]['name'] = item.name
                json_data[i]['place'] = item.place
                json_data[i]['length'] = item.length
                json_data[i]['status'] = item.status
                json_data[i]['price'] = item.price
                json_data[i]['date'] = item_time
        else:
            json_data = {'email': 'none'}

        return HttpResponse(json.dumps(json_data), content_type = "application/json")


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
            price = int(length) * 350
            new_contact=Contact(name=name,
                                email=email,
                                place=place,
                                length=length,
                                price=price,
                                status='в обработке')
            new_contact.save()
            mail = 'Уважаемый клиент, статус вашего заказа вы можете здесь http://127.0.0.1:8000/status'
            send_mail('Заказ сьемки у Weeding Photo Kiev',
                      mail,
                      'hector007@pochta.ru',
                      [email], fail_silently=False)
            return HttpResponseRedirect('/status/')

    return render(request, 'contact.html', context)