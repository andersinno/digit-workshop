from django.conf import settings
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('blog.urls')),
    path('da/', admin.site.urls),
]

if settings.DEBUG:
    # Serve media from development server
    from django.conf.urls.static import static
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
