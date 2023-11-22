
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('juegoderoles/',include('consultas.urls')),
    path('juegoderoles/admin/', admin.site.urls),
    path('juegoderoles/', include('polls.urls')),
    path('juegoderoles/', include('ros.urls')),
    path('juegoderoles/results/', include('results.urls')),
    path('juegoderoles/solicitud/',include('solicitud.urls')),
    path('juegoderoles/',include('homepage.urls')),    
   
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += staticfiles_urlpatterns()