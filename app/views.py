from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.

def home(request):
	tipos = TipoNegocio.objects.all()
	negocios = Negocio.objects.all()
	ciudades = Ciudad.objects.all()

	if request.GET:
		catched0 = get_object_or_404(TipoNegocio, tiponegocio= request.GET.get('tipo',''))
		catched1 = get_object_or_404(Ciudad, nombre= request.GET.get('ciudad',''))
		negocios2 = Negocio.objects.filter(tiponegocio = catched0 ).filter(ciudad = catched1)

		template = "index.html"
		return render_to_response(template,{"tipos":tipos,"negocios":negocios, "negocios2":negocios2, "ciudades":ciudades,"request":request})
	else:
		template = "home.html"
		return render_to_response(template,{"tipos":tipos,"negocios":negocios, "negocios2":negocios, "ciudades":ciudades,"request":request})




def tipo(request,id_tiponegocio):
	tipos = TipoNegocio.objects.all()
	negocios = Negocio.objects.all()
	ciudades = Ciudad.objects.all()

	if request.GET:
		catched0 = get_object_or_404(TipoNegocio, tiponegocio= request.GET.get('tipo',''))
		catched1 = get_object_or_404(Ciudad, nombre= request.GET.get('ciudad',''))
		negocios2 = Negocio.objects.filter(tiponegocio = catched0 ).filter(ciudad = catched1)

		template = "index.html"
		return render_to_response(template,{"tipos":tipos,"negocios":negocios, "negocios2":negocios2, "ciudades":ciudades,"request":request})
	else:
		catched = get_object_or_404(TipoNegocio, pk= id_tiponegocio)
		negocios2 = Negocio.objects.filter(tiponegocio = catched)
		template = "index.html"
		return render_to_response(template,{"tipos":tipos,"negocios":negocios, "negocios2":negocios2, "ciudades":ciudades,"request":request})

def nuevo(request):
	tipos = TipoNegocio.objects.all()
	negocios = Negocio.objects.all()
	ciudades = Ciudad.objects.all()
	if request.POST:
		form = NegocioForm(request.POST, request.FILES)
		if form.is_valid():
			neg = form.save(commit = False)
			neg.save()
			template = "home.html"
			return render_to_response(template,context=RequestContext(request,locals()))

	else:
		form = NegocioForm()
	template = "newneg.html"
	return render_to_response(template,context=RequestContext(request,locals()))
