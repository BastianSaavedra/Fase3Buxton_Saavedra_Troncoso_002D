from django.urls import path

from . import views


urlpatterns = [
   path('registro/', views.registro, name="registro"),
   path('usuario/', views.UserListView.as_view(), name="usuario"),
   path('nuevo-usuario/', views.nuevo_usuario, name="nuevo_usuario"),
   path('eliminar-usuario/<int:pk>/delete/', views.UserDeleteView.as_view(), name="eliminar_usuario"),
]
