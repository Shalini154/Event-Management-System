from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Include all URLs from your app (ems_app)
    path('', include('ems_app.urls')),
]
