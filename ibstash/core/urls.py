from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.front.urls')),
    path('', include('apps.apis.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
