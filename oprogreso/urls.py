from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about),
    path("home/", views.homepage, name='homepage'),
    path("bloques/", views.bloques_list, name='bloques'),
    path('marcar-actividad/<int:actividad_id>/', views.marcar_actividad, name='marcar_actividad'),
    path('accounts/', include('accounts.urls')),
    path('', include('accounts.urls')),
]
