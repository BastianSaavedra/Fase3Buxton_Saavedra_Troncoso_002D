#!/usr/bin/python3
from django.urls import path, include
from . import views

'''
      AQUI SE ENCUENTRAN LAS URLS DE LOS PRODUCTOS, TANTO LISTAS COMO
      LOS DEL CRUD, INDICANDO COMO PRIMER PARAMETRO EL URL QUE SE BUSCARA,
      COMO SEGUNDO, LA VISTA DE DONDE SE SACARA LA INFO Y COMO TERCER PARA-
      METRO, UN NOMBRE PARA PODER LLAMAR A LA URL DESDE OTRA PESTANNIA
   '''

urlpatterns = [
   
   #API
   
   
   # URL PRINCIPALES
   path('home', views.index, name="index"),
   path('placasmadres/', views.placamadre, name="placamadre"),
   path('procesadores/', views.procesador, name="procesador"),
   path('tarjetadevideo/', views.video, name="video"),
   path('ram/', views.rams, name="rams"),
   path('almacenamiento/', views.alma, name="alma"),
   path('fuenteDePoder/', views.fuente, name="fuente"),
   path('gabinetes/', views.gabo, name="gabo"),
   path('monitores/', views.moni, name="moni"),
   path('contacto/', views.contacto, name="contacto"),


   # URL PLACAS MADRE
   path('placasmadre/', views.PlacaListView.as_view(), name="placas"),
   path('placamadre/<int:pk>', views.PlacaDetailView.as_view(), name="placas-detail"),
   path('nueva-placa/', views.nueva_placa, name="nueva_placa"),
   path('modificar-placa/<id>/', views.modificar_placa, name="modificar_placa"),
   path('eliminar-placa/<id>/', views.eliminar_placa, name="eliminar_placa"),

   # URL PROCESADORES
   path('procesadore/', views.ProceListView.as_view(), name="procesadores"),
   path('procesador/<int:pk>', views.ProceDetailView.as_view(), name="procesadores-detail"),
   path('nuevo-procesador/', views.nuevo_procesador, name="nuevo_procesador"),
   path('modificar-procesador/<id>/', views.modicar_procesador, name="modificar_procesador"),
   path('eliminar-procesador/<id>/', views.eliminar_procesador, name="eliminar_procesador"),

   # URL GPU'S
   path('gpus/', views.GpuListView.as_view(), name="gpus"),
   path('gpu/<int:pk>', views.GpuDetailView.as_view(), name="gpu-detail"),
   path('nueva-gpu/', views.nuevo_gpu, name="nueva_gpu"),
   path('modificar-gpu/<id>/', views.modificar_gpu, name="modificar_gpu"),
   path('eliminar-gpu/<id>/', views.eliminar_gpu, name="eliminar_gpu"),

   # URL RAM
   path('rams/', views.RamListView.as_view(), name="memoriasram"),
   path('ram/<int:pk>', views.RamDetailView.as_view(), name="ram-detail"),
   path('nueva-ram/', views.nueva_ram, name="nueva_ram"),
   path('modificar-ram/<id>/', views.modificar_ram, name="modificar_ram"),
   path('eliminar-ram/<id>/', views.eliminar_ram, name="eliminar_ram"),

   # URL ALMACENAMIENTOS
   path('almacenamientos/', views.AlmacenamientoListView.as_view(), name="almacenamientos"),
   path('almacenamiento/<int:pk>', views.AlmacenamientoDetailView.as_view(), name="almacenamiento-detail"),
   path('nuevo-almacenamiento/', views.nuevo_almacenamiento, name="nuevo_almacenamiento"),
   path('modificar-almacenamiento/<id>/', views.modificar_almacenamiento, name="modificar_almacenamiento"),
   path('eliminar-almacenamiento/<id>/', views.eliminar_almacenamiento, name="eliminar_almacenamiento"),

   # URL FUENTES DE PODER
   path('fuentes/', views.FuentesPoderListView.as_view(), name="fuentes"),
   path('fuente-poder/<int:pk>', views.FuentesPoderDetailView.as_view(), name="fuente-detail"),
   path('nueva-fuente/', views.nueva_fuente, name="nueva_fuente"),
   path('modificar-fuente/<id>/', views.modificar_fuente, name="modificar_fuente"),
   path('eliminar-fuente/<id>/', views.eliminar_fuente, name="eliminar_fuente"),

   # URL GABINETE
   path('gabinetes/', views.GabineteListView.as_view(), name="gabinetes"),
   path('gabinete/<int:pk>', views.GabineteDetailView.as_view(), name="gabinete-detail"),
   path('nuevo-gabinete/', views.nuevo_gabinete, name="nuevo_gabinete"),
   path('modificar-gabinete/<id>/', views.modificar_gabinete, name="modificar_gabinete"),
   path('eliminar-gabinete/<id>/', views.eliminar_gabinete, name="eliminar_gabinete"),

   #URL MONITOR
   path('monitores/', views.MonitoreListView.as_view(), name="monitores"),
   path('monitor/<int:pk>', views.MonitoreDetailView.as_view(), name="monitor-detail"),
   path('nuevo-monitor/', views.nuevo_monitor, name="nuevo_monitor"),
   path('modificar-monitor/<id>', views.modificar_monitor, name="modificar_monitor"),
   path('eliminar-monitor/<id>', views.eliminar_monitor, name="eliminar_monitor"),
   
   
   
]

