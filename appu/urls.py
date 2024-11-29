from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import views if needed (e.g., for login)
from appu.views import login_view  # Include this line only if you're using login_view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('appu/', include('appu.urls')),  # App URLs (your app should have a 'urls.py')

    # Add additional paths here if you have any specific views for login or other features
    # path('login/', login_view, name='login'),  # Example login view (uncomment if necessary)
]

# Serve media files during development (e.g., images, uploaded files)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
