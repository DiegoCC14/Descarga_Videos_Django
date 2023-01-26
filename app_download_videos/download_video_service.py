from pathlib import Path
from pytube import YouTube

import re

exprecion_playlist = re.compile( "playlist" ) #buscamos playlist en la url

BASE_DIR = Path(__file__).resolve().parent
Carpeta_Descarga_Videos = BASE_DIR.parent/'Videos_Descargados'

def tipo_de_url( url ):
	pass

class Videos_Youtube():
	
	obj_yt = None

	titulo = None
	img = None
	url = None
	dir_video_guardado = None

	def __init__( self , url ):
		self.url = url
		self.obj_yt = YouTube( url )

	def set_info_video( self ):
		self.img = self.obj_yt.thumbnail_url
		self.titulo = self.obj_yt.title

	def save_video( self , tag_video_descargar ):
		if self.titulo == None and self.img == None:
			self.set_info_video()
		stream = self.get_Stream_video( int(tag_video_descargar) )
		stream.download( Carpeta_Descarga_Videos )
		self.dir_video_guardado = Carpeta_Descarga_Videos/(self.titulo+".mp4")
		return stream

	def get_Stream_video( self , itag ):
		return self.obj_yt.streams.get_by_itag( itag )
		
	def get_resolucion_de_video( self ):
		return [ {'resolution' : Stream.resolution , 'itag' : Stream.itag , 'filesize': Stream.filesize_mb } for Stream in self.obj_yt.streams.filter( progressive=True , file_extension='mp4' ) ]


if __name__ == "__main__":
	'''
	url_link = 'https://youtu.be/MPLN1ahXgcs?list=PLvq-jIkSeTUZ5XcUw8fJPTBKEHEKPMTKk'

	yt = YouTube( url_link )
	obj_video = Videos_Youtube( url_link )

	obj_video.set_info_video()
	print( obj_video.get_resolucion_de_video() )
	'''

	url_playlist = "https://www.youtube.com/playlist?list=PLm_3vnTS-pvkJTrWd87KRrLLlwo9IAgrJ"
	#yt = YouTube( url_playlist )

	
	print( exprecion.search(url_playlist) )

'''
print("Captions:")
print( yt.captions )
caption = yt.captions.get_by_language_code('es')

print( caption )

print( caption.generate_srt_captions() )
print("~~~~~~>>>>")
'''
'''
for tag in yt.streams.filter( progressive=True , file_extension='mp4' ):
	print( tag )
	print("")
print("Descargando~~>>>")
#tag.download( BASE_DIR )
'''
'''
p = Playlist('https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
print(f'Downloading: {p.title}')

for video in p.videos:
	video.streams.first().download()

for url in p.video_urls[:3]:
	print(url)
'''

'''
print(f'Downloading videos by: {c.channel_name}')
Downloading videos by: ProgrammingKnowledge
for video in c.videos:
	video.streams.first().download()
for url in c.video_urls[:3]:
	print(url)
'''