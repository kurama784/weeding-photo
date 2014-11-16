from django.contrib import admin, messages
from django.http import HttpResponse
from gallery.models import Album, Photo
from gallery.widgets import MultiFileInput
from django.forms import ModelForm
from django.utils.encoding import smart_str
from django.shortcuts import redirect
from sorl.thumbnail.admin import AdminImageMixin
from django_websocket import require_websocket

class AlbumAdmin(admin.ModelAdmin):
        list_display = ['title']

class PhotoAdminForm(ModelForm):
    class Meta:
        model = Photo
        widgets = {'image':MultiFileInput}

class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
        form = PhotoAdminForm
        list_display = ('image', 'get_thumbnail_html', )

        @require_websocket
        def echo_once(self, request, send):
            request.websocket.send(send)

        def add_view(self, request, *args, **kwargs):
            images = request.FILES.getlist('image', [])
            is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()
            files_count = len(images)


            if request.method == "GET" or len(images)<=1 or not is_valid:
                return super(PhotoAdmin, self).add_view(request, *args, **kwargs)
            for image in images:

                album_id = request.POST['album']
                try:
                    photo = Photo(album_id=album_id, image=image)
                    photo.save()
                except Exception, e:
                    messages.error(request, smart_str(e))
            return redirect('/admin/gallery/photo/')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)