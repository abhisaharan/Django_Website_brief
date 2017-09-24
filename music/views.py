from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.shortcuts import HttpResponse


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums, }       #context is something that a html page need to work. It is passes to html page
    return render(request, 'music/index.html', context)  # if only one key value in context. we can simply write {'all_albums': all_albums,}


def detail(request, album_id):
    #try:                                        ## if user enters album_id that doesnt exist
     #   album = Album.objects.get(pk=album_id)
   # except Album.DoesNotExist:
    #    raise Http404("Uh oh! It happens. Album is in process of making")
    album = get_object_or_404(Album, pk=album_id) # we can use this line instead of above code
    return render(request, 'music/detail.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song']) #https://www.youtube.com/watch?v=irH98-4eKmQ&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK&index=24
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album,
                                                     'error_message': 'you did not select valid song'})

    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})






