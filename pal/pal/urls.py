from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pal_new.views',
    # Examples:
    # url(r'^$', 'pal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pal/$', TemplateView.as_view(template_name = 'index.html')),
)
