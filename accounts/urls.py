from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/playlist/playlist_add', permanent=False), name='root_redirect'),
    path('login/', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)