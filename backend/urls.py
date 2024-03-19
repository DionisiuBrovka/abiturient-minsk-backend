from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-panel'),
    path('api/v1/', include('api.urls')),
    path('api/v2/', include('api_v2.urls'))
] 

if settings.DEBUG:  # new
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)