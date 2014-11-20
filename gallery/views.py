from django.shortcuts import render
from django.template import RequestContext
from gallery.models import Album, Photo
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from infinite_pagination import InfinitePaginator
from django.http import HttpResponse
import json

def home(request):
    context = RequestContext(request)
    context['photos'] = Album.objects.all()
    return render(request, 'index.html', context)

def photo(request):
    context = RequestContext(request)
    return render(request, 'detail.html', context)

class AlbumDetailView(DetailView):
    model = Album
    paginate_by = 1
    def get_context_data(self, **kwargs):

        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        print(context)
        ss = Album()
        photos = Photo.objects.filter(album=self.object.id)[:3]
        context['photos'] = photos
        return context

def json_album_detail(request):
    album = Album
    data = request.GET.get('album_id')
    count = request.GET.get('count')
    if request.method == "GET":
        #photos_all = Photo.objects.filter(album=data).length()
        #print photos_all
        photos = Photo.objects.filter(album=data)[3:count]
        if photos:
            i=0
            json_data = {}
            for item in photos:
                i=i+1

                json_data[i] = {}
                json_data[i]['url'] = item.image.url

        else:
            json_data = {'photos': 'none'}

        return HttpResponse(json.dumps(json_data), content_type = "application/json")

class AlbumListView(ListView):

    model = Album
    paginate_by = 3
    paginator_class = InfinitePaginator

    def get_context_data(self, **kwargs):

        context = super(AlbumListView, self).get_context_data(**kwargs)

        return context
