from django.urls import path
from .views import index, nosotros, perros, gatos, contactanos,login, indexadmin, save_gato, delete_gato, form_modgato, save_perro, form_modperro, delete_perro
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',index, name="index"),
    path('nosotros/',nosotros, name="nosotros"),
    path('perros/',perros, name="perros"),
    path('gatos/',gatos, name="gatos"),
    path('contactanos/',contactanos, name="contactanos"),
    path('login/',LoginView.as_view(template_name="core/admin/login.html"),name="login"),
    path('logout/',LogoutView.as_view(template_name="core/index.html"),name="logout"),
    path('indexadmin/',indexadmin, name="indexadmin"),
    path('save_gato/',save_gato, name="save_gato"),
    path('form_modgato/<id>',form_modgato, name="form_modgato"),
    path('delete_gato/<id>',delete_gato, name="delete_gato"),
    path('save_perro/',save_perro, name="save_perro"),
    path('form_modperro/<id>',form_modperro, name="form_modperro"),
    path('delete_perro/<id>',delete_perro, name="delete_perro"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)