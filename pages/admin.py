from django.contrib import admin
from pages.models import Contact, Settings
from pages.forms import PageForm, FlatPageAdmin
from django.shortcuts import redirect
from django.contrib.flatpages.models import FlatPage
from solo.admin import SingletonModelAdmin

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']

class PageAdmin(FlatPageAdmin):
    form = PageForm

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
admin.site.register(Settings, SingletonModelAdmin)