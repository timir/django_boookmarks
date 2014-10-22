from django.contrib import admin
from bookmarks.models import Bookmark
from bookmarks.models import Link
from bookmarks.models import Tag
from bookmarks.models import SharedBookmark

#admin.site.register(Bookmark)
admin.site.register(Link)
admin.site.register(Tag)
#admin.site.register(SharedBookmark)

#class Admin:
#    list_display = ('title', 'link', 'user')
     

class BookmarkAdmin(admin.ModelAdmin):
    # ...
    list_display = ('title', 'link', 'user')
    list_filter = ['user']
    search_fields = ['title']

admin.site.register(Bookmark, BookmarkAdmin)

class SharedBookmarkAdmin(admin.ModelAdmin):
    # ...
    list_display = ('bookmark', 'date', 'votes')


admin.site.register(SharedBookmark, SharedBookmarkAdmin)


