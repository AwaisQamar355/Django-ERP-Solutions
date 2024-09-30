from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authenticate.urls')),
    path('', include('pos.urls')),
    # path('finance/', include('finance.urls')),
    path('pos_admin/', include('pos_admin.urls')), 
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)