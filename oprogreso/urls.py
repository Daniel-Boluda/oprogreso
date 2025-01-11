from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about, name='about'),
    path("home/", views.homepage, name='home'),
    path("bloques/", views.bloques_list, name='bloques'),
    path('marcar-actividad/<int:actividad_id>/', views.marcar_actividad, name='marcar_actividad'),
    path('obtener_logros/', views.obtener_logros, name='obtener_logros'),
    path('accounts/', include('accounts.urls')),
    path('', views.homepage, name='home'),
]
