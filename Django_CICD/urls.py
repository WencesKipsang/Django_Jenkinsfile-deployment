
from django.contrib import admin
from django.urls import path, include
from cicd import urls as you

urlpatterns = [
    path('frs-jenkins/admin/', admin.site.urls),
    path('frs-jenkins/cicd/', include(you)),
]


# usermod -a -G sudo jenkins