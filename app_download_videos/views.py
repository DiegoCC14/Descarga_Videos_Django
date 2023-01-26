from pathlib import Path

from .download_video_service import Videos_Youtube

from django.shortcuts import render , redirect
from django.views import View
from django.http import JsonResponse , HttpResponse

from wsgiref.util import FileWrapper

BASE_DIR = Path(__file__).resolve().parent
Carpeta_Descarga_Videos = BASE_DIR.parent/'Videos_Descargados'

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt #Quitamos csrf_token


class Index( View ):
	
	def get( self , request ):
		return render(request, 'index.html' )


@method_decorator( csrf_exempt , name='dispatch' )
class Get_Info_URL( View ):
			
	def post( self , request ):
		request_Post = request.POST.dict()

		obj_video = Videos_Youtube( request_Post['url'] )
		obj_video.set_info_video() #ingresamos informacion a objeto

		return JsonResponse( {'img':obj_video.img , "titulo": obj_video.titulo , "resolucion_videos": obj_video.get_resolucion_de_video() } )		

@method_decorator( csrf_exempt , name='dispatch' )
class Download_Video( View ):
	
	def post( self , request ):
		request_Post = request.POST.dict()
		
		# Se descarga el video -->>
		obj_video = Videos_Youtube( request_Post['url'] )
		stream = obj_video.save_video( request_Post['itag'] )
		
		return JsonResponse( {'url_descarga': "descargar_video_name/" + obj_video.titulo + ".mp4" } )

def descarga_video( request , name_video ):
	
	try:
		# Envia el video a user ->>
		file = FileWrapper( open( Carpeta_Descarga_Videos/name_video , 'rb') )
		response = HttpResponse(file, content_type='video/mp4')
		response['Content-Disposition'] = f'attachment; filename={name_video}'
		return response
		# ----------------------->>
	except:
		return redirect( 'index' ) #Por un error redireccionamos al index
		
