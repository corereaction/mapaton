from django.shortcuts import render, get_object_or_404
from django.views.generic import View,TemplateView
import requests
from .models import Punto, Ruta
from django.http import HttpResponseRedirect



class HomeView(View):
	def get(self,request):
		template_name="main/index.html"

		return render(request,template_name)

class MapaView(View):
	def get(self,request):
		template_name="main/mapa.html"
		print('Entre a la vista!')
		rutas=Ruta.objects.all()

		headers = {'content-type': 'application/json; charset=UTF-8'}
		for ruta in rutas:
			ide=ruta.trailId
			elId='&trailId='+ide
			url="https://mapaton-public.appspot.com/_ah/api/dashboardAPI/v1/getTrailRawPoints?fields=points"+elId
			# payload = {"trailId": "4503921934467072" , "numberOfElements":30, "cursor":""}
			data = requests.post(url, headers=headers)
			data=data.json()
			trail=data["points"]
			print(data)
			print("Recibí respuesta")
			
			# Todo el desmadre de parsear
			ruta=get_object_or_404(Ruta,trailId=ide)
			# Si ya existe no hacemos nad

		   
			for dato in trail:
				latitud=dato['location']['latitude']
				print(latitud)

				try:
					punto = Punto.objects.get(latitude=latitud)
					print("Ya existe")
				except Punto.DoesNotExist:
					punto=Punto()
					punto.trail=ruta
					punto.ruta_id=ide
					print(dato['location']['latitude'])
					print(dato['location']['longitude'])
					punto.latitude=dato['location']['latitude']
					punto.longitude=dato['location']['longitude']
					punto.save()
					
					print("lo cree")
					

			
		return render(request,template_name)

class Rutas(View):
	def get(self,request):
		template_name="main/rutas.html"

		# Obtenemos todas las rutas
		headers = {'content-type': 'application/json; charset=UTF-8'}
		url='https://mapaton-public.appspot.com/_ah/api/dashboardAPI/v1/getAllTrails?fields=trails&numberOfElements=4110'
		data = requests.post(url, headers=headers)
		data=data.json()
		trails=data["trails"]

		rutasBuenas=[]
		for trail in trails:
			trailId=trail["trailId"]
			if trail['gtfsStatus']==2:
				rutasBuenas.append(trail)
				try:
					ruta = Ruta.objects.get(trailId=trailId)
					print("Ya existe")
				except Ruta.DoesNotExist:
					ruta=Ruta()
					ruta.trailId=trail["trailId"]
					ruta.originStationName=trail["originStationName"]
					ruta.destinationStationName=trail["destinationStationName"]
					ruta.transportType=trail["transportType"]
					ruta.maxTariff=trail["maxTariff"]
					ruta.photoUrl=trail["photoUrl"]
					ruta.notes=trail["notes"]
					ruta.totalMinutes=trail["totalMinutes"]
					ruta.totalMeters=trail["totalMeters"]
					ruta.gtfsStatus=trail["gtfsStatus"]
					ruta.save()
		

		
		return render(request,template_name)

class PrimeroUltimo(View):
	def get(self,request):
		template_name="main/ultimos.html"

		rutas=Ruta.objects.all()
		for ruta in rutas:
			headers = {'content-type': 'application/json; charset=UTF-8'}
			ide=ruta.trailId
			elId='&trailId='+ide
			url="https://mapaton-public.appspot.com/_ah/api/dashboardAPI/v1/getTrailRawPoints?fields=points"+elId
			# payload = {"trailId": "4503921934467072" , "numberOfElements":30, "cursor":""}
			data = requests.post(url, headers=headers)
			data=data.json()
			trail=data["points"]
			ruta.primerPuntolat=trail[0]['location']["latitude"]
			ruta.primerPuntolon=trail[0]['location']["longitude"]
			ruta.ultimoPuntolat=trail[-1]['location']["latitude"]
			ruta.ultimoPuntolon=trail[-1]['location']["longitude"]
			ruta.save()
		print("Puntos Guardados!")


		return render(request,template_name)

class Compara(View):
	def get(self,request):
		template_name="main/compara.html"
		rutas=Ruta.objects.all()
		context={
		'rutas':rutas,
		}

		return render(request,template_name,context)

	def post(self,request):
		template_name="main/compara.html"
		rutas=Ruta.objects.all()

		rutaid=request.POST.get('trail')
		print("EL id: ",rutaid)
		ruta=get_object_or_404(Ruta,trailId=rutaid)
		print("La Ruta: ",ruta)
		imgUrl=ruta.photoUrl
		try:
			puntos=ruta.puntos.all()
			print("Objeto encontrado!")
			print(puntos)
		except:
			print("No objeto")
		post=True
		context={
		'puntos':puntos,
		'rutas':rutas,
		'post':post,
		'img':imgUrl
		}


		return render(request,template_name,context)


