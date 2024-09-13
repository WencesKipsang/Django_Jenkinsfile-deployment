
from django.contrib import admin
from django.urls import path, include
from cicd import urls as you

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cicd/', include(you)),
]


# usermod -a -G sudo jenkins