from django.contrib import admin

from watchlist_app.models import StreamingPlatform,WatchList
# Register your models here.
admin.site.register((StreamingPlatform,WatchList))