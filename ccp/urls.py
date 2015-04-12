from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'form.views.home', name='home'),
    url(r'^form/(.*)/$', 'form.views.form', name='form'),
    url(r'^email_submit/$', 'form.views.mail', name='mail'),
    url(r'^submit/(.*)/$', 'form.views.submit', name='submit'),
    url(r'^pdf_download/(.*)/$','form.views.pdf_download',name='pdf'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}), )
