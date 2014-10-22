import os.path
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from bookmarks.views import *
from bookmarks.feeds import *
#from django.views.generic import direct_to_template
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)

feeds = {
  'recent': RecentBookmarks
}

urlpatterns = patterns('',
#Admin
  url(r'^admin/', include(admin.site.urls)),
#Browsing
  url(r'^$', main_page),
  url(r'^user/(\w+)/$', user_page),
  url(r'^tag/([^\s]+)/$', tag_page),
  url(r'^popular/$', popular_page),
  url(r'^bookmark/(\d+)/$', bookmark_page),
#Session management
  url(r'^login/$', 'django.contrib.auth.views.login'),
  url(r'^logout/$', logout_page),
  url(r'^register/$', register_page),
  url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
       { 'document_root': site_media }),
  url(r'^register/success/$', 'bookmarks.views.hello_template_simple'),
#Account management
  url(r'^save/$', bookmark_save_page),
  url(r'^vote/$', bookmark_vote_page),
#Tag Cloud
  url(r'^tag/$', tag_cloud_page),
#Bookmarks Search
  url(r'^search/$', search_page),  
# Ajax
  url(r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
# Comments
  url(r'^comments/', include('django.contrib.comments.urls')),
#Feeds
#  url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
  url(r'^feeds/(?P<url>.*)/$', RecentBookmarks()),
)
    




