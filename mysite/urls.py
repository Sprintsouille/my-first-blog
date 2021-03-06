"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # Cela signifie que pour chaque URL qui commence par admin/, Django affichera la vue correspondante.
    url(r'', include('blog.urls')),
    # Django va maintenant rediriger tout ce qui arrive sur "http://127.0.0.1:8000/" vers blog.urls puis regardera dans ce fichier pour y trouver la suite des instructions à suivre.
]
