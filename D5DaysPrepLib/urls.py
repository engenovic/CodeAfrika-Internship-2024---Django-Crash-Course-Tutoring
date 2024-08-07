from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls', namespace='students')),
    path('api/', include('students.api.urls', namespace='api')),
]
