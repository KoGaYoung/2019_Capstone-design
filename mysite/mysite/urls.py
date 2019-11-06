from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^chat/', include('chat.urls')),
    url(r'^admin/', admin.site.urls)
]
