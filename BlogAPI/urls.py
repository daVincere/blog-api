"""BlogAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

#  
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler400, handler403
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace="main")),
    path('', include(('accounts.urls', 'accounts'), namespace="accounts")),
    path('post/', include(('post.urls','post'), namespace="posts")),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Defining the new error handlers
handler400 = main_views.error400
handler403 = main_views.error403
handler404 = main_views.error404
handler500 = main_views.error500

admin.site.site_header = "mPharma Adminstration"
admin.site.site_title = "mPharma Adminstration"
