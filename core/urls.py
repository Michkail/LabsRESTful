"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from . import views

handler404 = views.custom_404
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("api/v1/user/", include("user.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("elysabeth/", views.elys_index, name="elys-index"),
    path("elysabeth/activities/", views.elys_activities, name="elys-activities"),
    path("elysabeth/date/", views.elys_date, name="elys-date"),
    path("elysabeth/dessert/", views.elys_dessert, name="elys-dessert"),
    path("elysabeth/food/", views.elys_food, name="elys-food"),
    path("elysabeth/lastpage/", views.elys_last_page, name="elys-last"),
    path("elysabeth/thankyou/", views.elys_thankyou, name="elys-thanks")
]

if settings.DEBUG is False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
