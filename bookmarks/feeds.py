from django.contrib.syndication.views import Feed
from bookmarks.models import Bookmark

class RecentBookmarks(Feed):
  title = 'Django Bookmarks | Recent Bookmarks'
  link = '/feeds/recent/'
  description = 'Recent bookmarks posted on Django Bookmarks'
  
  def items(self):
    return Bookmark.objects.order_by('-id')[:10]
