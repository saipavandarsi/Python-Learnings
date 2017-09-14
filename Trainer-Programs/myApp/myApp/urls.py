from django.conf.urls import patterns, include, url
from django.contrib import admin

from hello.views import hello
from register.views import signup, createuser

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/', hello),
	url(r'^signup/', signup),
	url(r'^create/', createuser),
)
