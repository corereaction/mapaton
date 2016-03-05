from django.shortcuts import render
from django.views.generic import View,TemplateView

class HomeView(View):
	def get(self,request):
		template_name="main/index.html"

		return render(request,template_name)