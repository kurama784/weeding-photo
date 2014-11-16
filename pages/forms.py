# *-* coding: utf-8 *-*
from django import forms
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Как можно к вам обращаться?')
    email = forms.EmailField(max_length=50, label='Действительный адрес электронной почты')
    place = forms.CharField(label='Место сьемки')
    length = forms.IntegerField(min_value=1, initial=1, label='Длительность сьемки')
    #content = forms.Textarea()

class ItemForm(forms.Form):
    email = forms.EmailField(label='Введите ваш email', max_length=50)

class PageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content': TinyMCE
        }

class PageAdmin(FlatPageAdmin):
    form = PageForm

class StatusForm(forms.Form):
    email = forms.EmailField(max_length=50, label='Введите ваш электронный адрес')
