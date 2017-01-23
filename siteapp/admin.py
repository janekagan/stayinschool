from django.contrib import admin
from .models import Album, Video, contactResponse, photoAlbum, Photo

# Register your models here.
admin.site.register(Album)
admin.site.register(Video)
admin.site.register(contactResponse)
admin.site.register(photoAlbum)
admin.site.register(Photo)
