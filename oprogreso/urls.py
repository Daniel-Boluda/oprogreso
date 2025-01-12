from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about, name='about'),
    path("bloques_list/", views.bloques_list, name='bloques_list'),
    path('marcar-actividad/<int:actividad_id>/', views.marcar_actividad, name='marcar_actividad'),
    path('obtener_logros/', views.obtener_logros, name='obtener_logros'),
    path('accounts/', include('accounts.urls')),
    path('', views.bloques_list, name='bloques_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)