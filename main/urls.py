from django.conf.urls import url
from . import views

urlpatterns=[

	url(r'^$',views.HomeView.as_view(),name='_home'),
	url(r'^mapa/$',views.MapaView.as_view(),name='mapa'),
	url(r'^rutas/$',views.Rutas.as_view(),name='rutas'),
	url(r'^ultimos/$',views.PrimeroUltimo.as_view(),name='ultimos'),
	url(r'^compara/$',views.Compara.as_view(),name='compara'),
	url(r'^custom/$',views.Custom.as_view(),name='custom'),
	url(r'^gastro/$',views.Gastro.as_view(),name='gastro'),

	
]